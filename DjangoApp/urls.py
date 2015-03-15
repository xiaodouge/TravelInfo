from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','LV.views.home'),
    url(r'^upload/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'upload/'}),
    url(r'^(?P<id>\d+)/$', 'LV.views.detail', name='detail'),
)
