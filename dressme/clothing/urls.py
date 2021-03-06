from django.conf.urls import url, include
from clothing.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^user_login/$', user_login, name='user_login'),
    url(r'^register/$', register, name='register'),
    url(r'^authorize/$', authorize, name='authorize'),
    url(r'^calendarHelper/$', calendarHelper, name='calendarHelper'),
    url(r'^calendar/$', calendar, name='calendar'),
    url(r'^logout/$', logout_view, name='logout_view'), 
    # url(r'^eventAdder/$', eventAdder, name='eventAdder'), 
    # url(r'^eventAuth/$', eventAuth, name='eventAuth')
]