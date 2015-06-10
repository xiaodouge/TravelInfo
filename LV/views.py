#coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from LV.models import Articles
from LV.models import User
from django.http import Http404
from datetime import datetime
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.save()
            #返回注册成功页面

            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/home/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})

#定义表单模型
class ArticlesForm(forms.Form):
    title = forms.CharField(label='标题：',max_length = 50)
    country = forms.CharField(label='国家：',max_length = 50)
    city = forms.CharField(label='城市：',max_length = 50)
    address = forms.CharField(label='地址：',max_length = 50)
    tick = forms.CharField(label='票价：',max_length=50)
    open_time = forms.CharField(label='开放时间：',max_length = 50)
    category = forms.CharField(label='分类：',max_length = 50)
    content = forms.CharField(label='内容：')
    headImg = forms.FileField(label='插图：')


# Create your views here.
def addinfo(request):
    if request.method == "POST":
        infoform = ArticlesForm(request.POST,request.FILES)
        if infoform.is_valid():
            #获取表单信息
            title = infoform.cleaned_data['title']
            country = infoform.cleaned_data['country']
            city = infoform.cleaned_data['city']
            address = infoform.cleaned_data['address']
            tick = infoform.cleaned_data['tick']
            open_time = infoform.cleaned_data['open_time']
            category = infoform.cleaned_data['category']
            content = infoform.cleaned_data['content']
            headImg = infoform.cleaned_data['headImg']
            pubuser = request.COOKIES.get('username','')

            #将表单写入数据库
            info = Articles()
            info.title = title
            info.country = country
            info.city = city
            info.address = address
            info.tick = tick
            info.open_time = open_time
            info.category = category
            info.content = content
            info.headImg=headImg
            info.pubuser=pubuser
            info.save()
            response = HttpResponseRedirect('/home/')
            return response
    else:
        infoform = ArticlesForm()
    return render_to_response('addinfo.html',{'infoform':infoform})


#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/home/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    if request.user.is_authenticated:
        state = '已登录'
    else:
        state = '未登录'
    return render_to_response('index.html' ,{'username':username,'state':state})

#退出
def logout(req):
    response = HttpResponseRedirect('/home/')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def address_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            username = request.COOKIES.get('username','')
            if username:
                login_state = True
            else:
               login_state = False
            return render(request, 'about.html')
        else:
            username = request.COOKIES.get('username','')
            if username:
                login_state = True
            else:
               login_state = False
            post_list = Articles.objects.filter(title__icontains=s);
            country_list = Articles.objects.values("country").distinct()
            country_list.query.group_by = ['country']

            if len(post_list) == 0:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': True,'login_state':login_state,'username':username})
            else:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': False,'login_state':login_state,'username':username})

    return redirect('/')


def choose_country(request):
    if 'country' in request.POST:
        s = request.POST['country']
        if not s:
            username = request.COOKIES.get('username','')
            if username:
              login_state = True
            else:
                login_state = False
            return render(request, 'about.html')

        else:
            username = request.COOKIES.get('username','')
            if username:
              login_state = True
            else:
                login_state = False
            post_list = Articles.objects.filter(country__iexact=s)  # contains
            country_list = Articles.objects.values("country").distinct()
            country_list.query.group_by = ['country']

            if len(post_list) == 0:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': True,'login_state':login_state,'username':username})
            else:
                return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list, 'error': False,'login_state':login_state,'username':username})

    return redirect('/')

def userhome(request):
    try:
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
        posts = Articles.objects.filter(pubuser__iexact=username)
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
        paginator = Paginator(posts,5)
        page = request.GET.get('page')
        post_list = paginator.page(page)

    except Articles.DoesNotExist:        
        raise Http404
    except PageNotAnInteger :
        post_list = paginator.page(1)
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False

    return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list,'login_state':login_state,'username':username})



def detail(request, id):
    try:
        post = Articles.objects.get(id=str(id))
        country_list = Articles.objects.values("country").distinct()
        country_list.query.group_by = ['country']
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
    except Articles.DoesNotExist:
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
        raise Http404


    return render(request, 'post.html', {'post': post, 'country_list': country_list,'login_state':login_state,'username':username})


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
        paginator = Paginator(posts,5)
        page = request.GET.get('page')
        post_list = paginator.page(page)
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
    except Articles.DoesNotExist:        
        raise Http404
    except PageNotAnInteger :
        post_list = paginator.page(1)
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False

    return render(request, 'home.html', {'post_list': post_list, 'country_list': country_list,'login_state':login_state,'username':username})


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
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
    except Articles.DoesNotExist:
        username = request.COOKIES.get('username','')
        if username:
            login_state = True
        else:
            login_state = False
        raise Http404
    return render(request, 'about.html', {'about': about, 'country_list': country_list,'login_state':login_state,'username':username})

