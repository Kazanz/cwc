from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'codewithchrist.views.landing', name='landing'),
    url(r'^sign-up/$', 'codewithchrist.views.sign_up_form', name='sign-up-form'),
    url(r'^admin/', include(admin.site.urls)),
)
