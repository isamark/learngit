#coding=utf-8
from django.db import models

#用户
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=64)
    ureceiver = models.CharField(max_length=20,default='')
    uadress =  models.CharField(max_length=100,default='')
    upostcode = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')

    def __str__(self):
        return self.uname










