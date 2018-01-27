from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.models import OnlineJudge
from utils.ojurl import showURL
from .models import Problem, ProblemStatus, ProblemInSet, ProblemSet


@login_required
def problem_set_page(request):
    set = ProblemSet.objects.get(id=int(request.GET['setId']))
    pList = set.hasProblem.all().order_by("probId")
    for prob in pList:
        try:
            if ProblemStatus.objects.get(problem=prob, realUser=request.user).is_AC:
                prob.state = "Accepted"
            else:
                prob.state = "Attempted"
        except ProblemStatus.DoesNotExist:
            prob.state = "Fresh"

    return render(request, "set_list.html", {
        'set': set,
        'prob_list': pList,
        'is_creater': request.user == set.setCreator,
        'oj_list': OnlineJudge.objects.all(),
    })


@login_required
def add_problem_set(request):
    ProblemSet.objects.get_or_create(setName=request.POST["name"], setCreator=request.user,
                                     author=request.POST["author"])
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def insert_problem_to_set(request):
    OJ = OnlineJudge(name=request.POST['OJname'])
    prob = Problem.objects.get_or_create(
        platform=OJ,
        probId=request.POST['prob_id'],
        url=showURL(request.POST['OJname'], request.POST['prob_id'])
    )[0]
    set = ProblemSet(id=int(request.POST["set_id"]))
    print(prob.title, set.setName)
    ProblemInSet.objects.get_or_create(problem=prob, set=set)
    return redirect(request.META.get('HTTP_REFERER'))
# Create your views here.
