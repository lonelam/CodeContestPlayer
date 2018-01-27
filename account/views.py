from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from problem.models import ProblemStatus
from .models import OJUser, OnlineJudge
from .tasks import user_all_status


def login_page(request):
    if request.method == 'POST':
        if 'Login' in request.POST:
            user = authenticate(username=request.POST['uTxtName'], password=(request.POST['uTxtPass']))
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('/profile/')
            else:
                return HttpResponse('Debug: Login failed')
        elif 'Register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['uTxtName'])
            except:
                user = User.objects.create_user(username=request.POST['uTxtName'], password=(request.POST['uTxtPass']))
                return HttpResponse('Debug: Register Success')
        elif 'Delete' in request.POST:
            try:
                user = User.objects.get(username=request.POST['uTxtName'])
                user.delete()
                return HttpResponse('Debug: Delete Success')
            except:
                print('User not Exist')
    return render(request, 'login.html')


@login_required
def profile_page(request):
    accList = OJUser.objects.filter(realUser=request.user)
    probList = ProblemStatus.objects.filter(realUser=request.user)
    return render(request, "profile.html", {
        'user': request.user,
        'accList': accList,
        'oj_list': OnlineJudge.objects.all(),
        'prob_list': probList.order_by("problem__probId"),
    })


@login_required
def add_account(request):
    oj = OnlineJudge(name=request.POST["OJname"])
    newAccount = OJUser.objects.get_or_create(realUser=request.user, platform=oj, userId=request.POST["new_id"])
    user_all_status.delay(request.POST["new_id"], request.POST["OJname"], request.user.username)
    return redirect(request.META.get('HTTP_REFERER'))
