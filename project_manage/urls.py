from django.conf.urls import patterns, include, url
from view import index,deploy,call_live,show_call_live
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', index),
    url(r'^deploy/$', deploy),
    url(r'^show_call_live/$', show_call_live),
    url(r'^call_live/$', call_live),
    url(r'^admin/', include(admin.site.urls)),
)
