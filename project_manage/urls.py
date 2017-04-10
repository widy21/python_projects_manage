from django.conf.urls import patterns, include, url
from view import index,deploy
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', index),
    url(r'^deploy/$', deploy),
    url(r'^admin/', include(admin.site.urls)),
)
