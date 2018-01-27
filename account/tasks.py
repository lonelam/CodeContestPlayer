from __future__ import absolute_import, unicode_literals

import requests
from bs4 import BeautifulSoup
from celery import shared_task

from problem.models import Problem, ProblemStatus
from utils.ojurl import showURL
from .models import OnlineJudge, OJUser, User

status_url = {
    'hdu': '/status.php',
}
default_param = {'user': '', 'pid': 0, 'lang': 0, 'status': 0}
base_url = {
    'hdu': 'http://acm.hdu.edu.cn',
}


# celery -A CodeContestPlayer worker --pool=solo -l info
@shared_task
def user_all_status(username, platform, identity):
    OJ = OnlineJudge(name=platform)
    user = User.objects.get(username=identity)
    acc = OJUser.objects.get(platform=OJ, userId=username, realUser=user)
    print(OJ, username, acc)
    ret = []

    if platform == 'hdu':
        param = {'user': username, 'last': 1}
        while True:
            status_response = requests.get(base_url[platform] + status_url[platform], param)
            soup = BeautifulSoup(status_response.text, "lxml")
            status_table = list(soup.find('table', cellspacing="2"))[2:]
            status_page = [[list(s.strings)[0] for s in line.find_all('td')] for line in status_table]
            # print([[s for s in line.find_all('td')] for line in status_table])
            # print(status_page)
            ret.extend(status_page)
            # print('debug %d, this page cnt: %d' % (param['last'], len(status_page)))
            if len(status_page) < 15:
                break
            param['last'] = int(status_page[0][0].string) + 1
        for record in ret:
            print(record)
            p = ProblemStatus.objects.get_or_create(
                problem=Problem.objects.get_or_create(
                    platform=OJ,
                    probId=record[3],
                    url=showURL(platform, record[3]))[0],
                realUser=user,
            )

            if record[2] == 'Accepted':
                p[0].is_AC = True
                p[0].save()
    elif platform == 'cf':
        param = {''}
        status_response = requests.get()
