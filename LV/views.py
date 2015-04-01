from django.shortcuts import render, redirect
from django.http import HttpResponse
from LV.models import Articles
from django.http import Http404;
from datetime import datetime
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def address_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'about.html')
        else:
            post_list = Articles.objects.filter(title__icontains=s);
            country_list = Articles.objects.values("country").distinct()
            country_list.query.group_by = ['country']
            if len(post_list) == 0:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': True})
            else:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': False})

    return redirect('/')


def choose_country(request):
    if 'country' in request.POST:
        s = request.POST['country']
        if not s:
            return render(request, 'about.html')
        else:
            post_list = Articles.objects.filter(country__iexact=s)  # contains
            country_list = Articles.objects.values("country").distinct()
            country_list.query.group_by = ['country']
            if len(post_list) == 0:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': True})
            else:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': False})

    return redirect('/')


def detail(request, id):
    try:
        post = Articles.objects.get(id=str(id))
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'country_list': country_list})


"""
def country(request,country):
    try:
        country_post_list = Articles.objects.filter(country=str(country))
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'country.html', {'post': country_post_list})
"""


def home(request):
    try:
        posts = Articles.objects.all()
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
        paginator = Paginator(posts,1)
        page = request.GET.get('page')
        post_list = paginator.page(page)

    except Articles.DoesNotExist:
        raise Http404
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list})


"""
def archives(request):

    try:
        post_list = Articles.objects.all()
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,'country_list': country_list})
"""


def about(request):
    try:
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'about.html', {'about': about, 'country_list': country_list})

