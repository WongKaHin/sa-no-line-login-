from email.policy import default
from operator import mod
from pyexpat import model
from re import T
from statistics import mode
from this import d
from django.db import models
import time

# Create your models here.

class Member(models.Model):
    memid = models.AutoField(primary_key=True)
    phone = models.IntegerField(default=0)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    



class History(models.Model):
    ordid = models.AutoField(default=0,primary_key=True)
    memid = models.IntegerField(default=0)
    cdate = models.DateField() 
    gpoint = models.IntegerField(default=0)
    c_amount = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    appname = models.CharField(max_length=100)

class behavior(models.Model):
    behid = models.IntegerField(default=0, primary_key=True)
    beh = models.CharField(max_length=100)
    npoint = models.IntegerField(default=0)

class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    memid = models.IntegerField()
    edate = models.DateField(auto_now=True)
    npoint = models.IntegerField(default=0)
    elist = models.CharField(max_length=100)

class question(models.Model):
    memid = models.IntegerField(default=0)
    rdate = models.DateTimeField(auto_now=True)
    disc = models.CharField(max_length=1000)