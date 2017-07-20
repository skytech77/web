from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^login/$', views.test, name='login'),
    url(r'^singup/$', views.test, name='singup'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.test, name='question_detail'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.test, name='popular'),
    url(r'^new/$', views.test, name='new'),
]