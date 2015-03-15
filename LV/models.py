#coding:utf-8
from django.db import models

# Create your models here.


class Articles(models.Model) :
    title = models.CharField(max_length = 50, blank = True)  #title
    country = models.CharField(max_length = 50, blank = True)  #country
    city = models.CharField(max_length = 50, blank = True)  #city
    address = models.CharField(max_length = 50, blank = True)  #address
    tick = models.CharField(max_length = 50, blank = True)  #tick
    open_time = models.CharField(max_length = 50, blank = True)  #opentime
    category = models.CharField(max_length = 50, blank = True)  #category
    date_time = models.DateTimeField(auto_now_add = True)  #publishdate
    content = models.TextField(blank = True, null = True)  #content
    headImg = models.FileField(upload_to = 'upload/',blank = True)

    def __unicode__(self) :
        return self.title

    class Meta:  #order by date desc
        ordering = ['-date_time']

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
