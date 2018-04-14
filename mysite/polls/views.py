# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#简单回显，没有实现数据样式分离
def index(request):
    return HttpResponse("Hello,elio.This is your first Django project")

#数据库测试，添加、删除等
def testdb(request):
    test1 = models.Test(name='zxy')
    test1.save()
    #list = models.Test.objects.order_by("id").reverse()[0:3]
    list = models.Test.objects.filter(name='test')
    list.delete()
    all = models.Test.objects.all()
    return render(request,"test.html",{"data":all})
#    return render(request,"index.html",{"data":user_list})
  #  return HttpResponse("{% for i in list %} <li>{{ i.name }}</li> {% endfor %}" )
  #  return HttpResponse("<p>数据添加成功!<p>")

#表单
def search_form(request):
    return render_to_response('search_form.html')

#接收请求数据
def search(request):
   # request.encoding='utf-8'
    if 'q' in request.GET:
        message = u'你输入的内容：' + request.GET['q']
    else:
        message = '你提交了空表'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    ctp={}
    ctp.update(csrf(request))
    #if request.POST:
       #ctx['rlt'] = request.POST['q']
       #ctp['rlt'] = request.POST['p']
    if request.POST:
        insert = models.user_pwd(user=request.POST['q'],password=request.POST['p'])
        if models.user_pwd.objects.filter(user=request.POST['q']):
            match = models.user_pwd.objects.filter(user=request.POST['q'])
            return render(request, "post_exist.html", {"data": match})
            #return HttpResponse("user already exists!")
        else:
            insert.save()
        #return render(request, "post.html", ctx)
        #password1 = models.user_pwd(password=request.POST['p'])
        #password1.save()
    #else:
    #    return HttpResponse("Can't insert empty data")
    all = models.user_pwd.objects.all()
    return render(request, "post.html", {"data": all})
#    res.append(render(request, "post.html", ctp))
#    return res

#@login_required
def tasklist(request):
    username=request.user.username
    if len(Dba.objects.filter(username=username)) == 0: #User is not DBA, only shows his/her own tasklist
        userid=User.objects.filter(username=username)
        lines = Task.objects.filter(creater=userid).order_by("-id")
    else:   #User is DBA, shows all tasklist
        lines = Task.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('tasklist.html', RequestContext(request, {'lines': show_lines,}))