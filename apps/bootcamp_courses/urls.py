from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^create$', views.create, name='add_course'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove_course'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_course'),
  ]
