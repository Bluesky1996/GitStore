# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib import auth
from .models import *
import time

def register(request):
    if request.POST:
        teamName = request.POST['teamName']
        password = request.POST['password']
        username = request.POST['username']
        point = 0

        st1 = request.POST['st1']
        stnum1 = request.POST['stnum1']
        ##qq1 = request.POST['qq1']
        num1 = request.POST['num1']

        st2 = request.POST['st2']
        stnum2 = request.POST['stnum2']
        ##qq2 = request.POST['qq2']
        num2 = request.POST['num2']

        st3 = request.POST['st3']
        stnum3 = request.POST['stnum3']
        ##qq3 = request.POST['qq3']
        num3 = request.POST['num3']
        cheakteamName = team.objects.filter(teamName=teamName)
        if(len(cheakteamName)>0):
            error = []
            error.append('队伍名注册过了哦~')
            return render_to_response('regist.html',{"error":error[0]})
        cheakusername = team.objects.filter(username = username)
        if(len(cheakusername)>0):
            error1 = []
            error1.append('用户名注册过了哦~')
            return render_to_response('regist.html', {"error1": error1[0]})
        teams = team.objects.create(teamName = teamName,password = password,username = username,point = point, \
                                st1 = st1,stnum1 = stnum1,num1 = num1, \
                                st2=st2, stnum2=stnum2, num2=num2, \
                                st3=st3, stnum3=stnum3, num3=num3,)
        user = User.objects.create_user(username, '1@qq.com', password)
        user.save()
        teams.save()
        return HttpResponseRedirect("../login/")
    else:
        return render_to_response("regist.html")
    #try:
    #    check = team.objects.get( username=username)
    #except:
     #   return HttpResponse('注册失败')

    #try:
    #   user = User.objects.create_user(username, '1@qq.com', password)
    #except:
    #    return HttpResponse('创建失败')

    #return HttpResponse('注册成功')





def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userResult = team.objects.filter(username=username, password=password)
        if(len(userResult)>0):
            try:
                user = authenticate(username=username, password=password)
                auth.login(request, user)
            except:
                return render_to_response('login.html')
            return HttpResponseRedirect("../challenge/")
        else:
            error = []
            error.append('用户名或密码不正确')
            return render_to_response('login.html',{'error':error[0]})
    return render_to_response('login.html')

def rank(request):
    result = team.objects.order_by('-point')
   # return HttpResponse(result[0].teamName)
    return render(request,'rank.html',{'result':result})



def out(request):

    logout(request)
    #return HttpResponse('Logout Success!')
    return render(request, 'index.html')

def getNotice(request):
    notices = notice.objects.all()
    return render(request, 'notice.html', {'notices': notices})



def getChallenge1(request):
    lists = []
    user = team.objects.filter(username = request.user.username)
    challenges = challenge.objects.all()
    for foo in challenges:
        check = log.objects.filter(name=request.user.username,check=True,challengeid=foo.id)
        if len(check) > 0:
             clgs = clg()
             clgs.id = foo.id
             clgs.title = foo.title
             clgs.info = foo.info
             clgs.type = foo.type
             clgs.point = foo.point
             clgs.check = True
             lists.append(clgs)
        else:
            clgs = clg()
            clgs.id = foo.id
            clgs.title = foo.title
            clgs.info = foo.info
            clgs.type = foo.type
            clgs.point = foo.point
            clgs.check = False
            lists.append(clgs)

    #return HttpResponse(error)
    return render(request,'challenge.html',{'challenges':lists,'user':user})

def submitFlag(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.user.username
        flag = request.POST['flag']

        try:
            teams = team.objects.get(username = name)
            challenges = challenge.objects.get(id = id)
        except:
            return HttpResponse('你还没有登录呢~')

        history = log.objects.filter(challengeid = id,name = name,check=True)
        if len(history) > 0:
            return HttpResponse('你已经提交过此题flag~')

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if challenges.flag != flag:
            logs = log.objects.create(challengeid=id, name=name, date=date,flag=flag,
                                  ip=request.META['REMOTE_ADDR'], check = False)
            return HttpResponse('好像不对~')


        logs = log.objects.create(challengeid=challenges.id,date=date,name=name, flag=flag, ip=request.META['REMOTE_ADDR'],check = True )
        teams.point = teams.point + challenges.point
        teams.save()
        return HttpResponse('提交成功~')

    return render_to_response("challenge.html")

#后台功能

def updateNotice(request):
    if request.META['REMOTE_ADDR'] != '127.0.0.1':
        return HttpResponse('404')
    if request.method == 'POST':
        no = request.POST['notice']
        #info = request.POST['notice']
        notices = notice.objects.create(info = no)
        notices.save()
        #return HttpResponse('lalla')
        return HttpResponseRedirect("../notice/")
    return render_to_response("adminpushNotice.html")

def updateChallenge(request):
    if request.META['REMOTE_ADDR'] != '127.0.0.1':
        return HttpResponse('404')
    if request.method == 'POST':
        title = request.POST['name']
        type = request.POST['category']
        info = request.POST['desc']
        point = request.POST['value']
        flag = request.POST['key']
        chal = challenge.objects.create(title=title,type=type,info=info,point=point,flag=flag)
        chal.save()
        # return render_to_response("admincheckChallenge.html")
        return HttpResponseRedirect("../challenge/")
        # return HttpResponse('lalla')
    return render_to_response("adminpushChallenge.html")

def index1(request):
	return render(request,'index.html')


class clg(object):
    id = '0'
    title = 'title'
    info = 'info'
    point = 'point'
    type = 'type'
    check = False
