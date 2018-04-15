# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.db import models

#from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publishec')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choise_text

class Test(models.Model):
    name = models.CharField(max_length=20)

class user_pwd(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Classes(models.Model):
    """
    班级表,男
    """
    titile = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    """
    老师表，女
    """
    name = models.CharField (max_length=32)

"""
cid_id  tid_id
 1    1
 1    2
 6    1
 1000  1000
"""
# class C2T(models.Model):
#     cid = models.ForeignKey(Classes)
#     tid = models.ForeignKey(Teachers)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'
