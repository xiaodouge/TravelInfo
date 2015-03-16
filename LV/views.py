from django.shortcuts import render
from django.http import HttpResponse
from LV.models import Articles
from django.http import Http404;
from datetime import datetime
# Create your views here.

def detail(request, id):
    try:
        post = Articles.objects.get(id=str(id));
    except Articles.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def countries(request,sel_country):
    try:
        post_list = Articles.objects.get(country=sel_country);
    except Articles.DoesNotExist:
        raise Http404
    return render(request,'countries.html',{'post_list':post_list})

def home(request):
    post_list = Articles.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def about(request):
    return render(request,'about.html',{'about':about})
