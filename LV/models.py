#coding:utf-8
from django.db import models
from django import forms
from django.contrib import admin
# Create your models here.


class Articles(models.Model) :
    title = models.CharField('标题',max_length = 50, blank = True)  #title
    country = models.CharField('国家',max_length = 50, blank = True)  #country
    city = models.CharField('城市',max_length = 50, blank = True)  #city
    address = models.CharField('地址',max_length = 50, blank = True)  #address
    tick = models.CharField('票价',max_length = 50, blank = True)  #tick
    open_time = models.CharField('开放时间',max_length = 50, blank = True)  #opentime
    category = models.CharField('分类',max_length = 50, blank = True)  #category
    date_time = models.DateTimeField('更新时间',auto_now_add = True)  #publishdate
    content = models.TextField('内容',blank = True, null = True)  #content
    headImg = models.FileField('插图',upload_to = 'upload/',blank = True)
    pubuser = models.CharField('发布者',max_length = 50, default='管理员')

    def __unicode__(self) :
        return self.title

    class Meta:  #order by date desc
        ordering = ['-date_time']

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __unicode__(self):
        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(User,UserAdmin)

"""
class INFO(models.Model) :
    title = models.CharField(max_length = 100)  #title
    date = models.DateTimeField(auto_now_add = True)  #date
    content = models.TextField(blank = True, null = True)  #content

    def __unicode__(self) :
        return self.title

    class Meta:  #order by date desc
        ordering = ['-date']
"""
