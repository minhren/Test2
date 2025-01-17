from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete(\d+)$', views.delete),
    url(r'^areas$', views.areas),
    url(r'^login$', views.login),
    url(r'^login_check', views.login_check),
]
