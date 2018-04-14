# -*- coding: utf-8 -*-

from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse

#user_list = [
#    {"user":"jack","pwd":"abc"},
#    {"user":"elio","pwd":"AB12"}
#]
def index(request):
    if request.method == "GET":
        username = 'HL'
        #password = request.GET.get("password",None)
        password = 'none'
        models.UserInfo.objects.create(user=username, pwd=password)
        #print(username,password)
 #   if request.method != "POST":
 #      models.UserInfo.objects.create(user=request.method,pwd='3')
    user_list = models.UserInfo.objects.all()
    #return HttpResponse("hello world!")
    return render(request,"index.html",{"data":user_list})

def test(request):
#    return HttpResponse("Hello,elio.This is your first Django project")
    context = {}
    context['hello'] = 'Hello world!'
    #return render(request, "hello.html", context)
    return render(request,'hello.html',context)
# Create your views here.
