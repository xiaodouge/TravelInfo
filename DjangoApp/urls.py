from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DjangoApp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       #url(r'^(?P<country>\D+)/$', 'LV.views.country', name='country'),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'static/'}),
                       url(r'^$', 'LV.views.home'),
                       url(r'^home/$', 'LV.views.home'),
                       url(r'^about$', 'LV.views.about'),
                       #url(r'^archives/$', 'LV.views.archives', name = 'archives'),
                       url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'upload/'}),
                       url(r'^(?P<id>\d+)/$', 'LV.views.detail', name='detail'),
                       url(r'^search/$', 'LV.views.address_search',name = 'address_search'),
                       url(r'^country/$','LV.views.choose_country', name = 'choose_country'),
                       url(r'^userhome/$','LV.views.userhome', name = 'userhome'),
                       url(r'^register/$','LV.views.register',name = 'register'),
                       url(r'^login/$','LV.views.login',name = 'login'),
                       url(r'^logout/$','LV.views.logout',name = 'logout'),
                       url(r'^index/$','LV.views.index',name = 'index'),
                       url(r'^addinfo/$','LV.views.addinfo',name = 'addinfo'),
)
