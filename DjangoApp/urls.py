from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'static/'}),
    url(r'^$','LV.views.home'),
     url(r'^about$','LV.views.about'),
    url(r'^(?P<sel_country>\D+)$','LV.views.countries',name="countries"),

    url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'upload/'}),
    url(r'^(?P<id>\d+)/$', 'LV.views.detail', name='detail'),
)
