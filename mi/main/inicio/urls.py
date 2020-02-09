from django.conf.urls import url,re_path
from django.urls import path, include
from inicio import views

urlpatterns =[
url(r'^$', views.HomeView,name="main"),
]