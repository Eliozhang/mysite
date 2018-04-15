from django.shortcuts import render
from django.shortcuts import redirect
from . import models
import time

def get_classes(request):
    cls_list = models.Book.objects.all()
    return render(request, 'get_classes.html', {'cls_list': cls_list})


def add_classes(request):
    if request.method == "GET":
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        #ititle = request.POST.get(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        #time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        models.Book.objects.create(title=title,author=author,date=time.strftime('%Y-%m-%d',time.localtime(time.time())))
        #models.Book.objects.create(author=author)
        #models.Book.objects.create(date=time.strftime('%Y-%m-%d',time.localtime(time.time())))
        return redirect('/polls/get_classes.html')


def del_classes(request):
    nid = request.GET.get('nid')
    models.Book.objects.filter(id=nid).delete()
    return redirect('/polls/get_classes.html')


def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Book.objects.filter(id=nid).first()
        return render(request, 'edit_classes.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        author = request.POST.get('author')
        date = request.POST.get('date')
        models.Book.objects.filter(id=nid).update(title=title)
        models.Book.objects.filter(id=nid).update(author=author)
        models.Book.objects.filter(id=nid).update(date=date)
        return redirect('/polls/get_classes.html')

def find_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Book.objects.filter(id=nid).first()
        return render(request, 'find_classes.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        author = request.POST.get('author')
        date = request.POST.get('date')
        if request.POST.get('title'):
            cls_list = models.Book.objects.filter(title=title)
        if request.POST.get('author'):
            cls_list = models.Book.objects.filter(author=author)
        if request.POST.get('date'):
            cls_list = models.Book.objects.filter(date=date)
        return render(request, 'get_classes.html', {'cls_list': cls_list})
