__author__ = 'polakj'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^email/$', views.email, name='email'),
]