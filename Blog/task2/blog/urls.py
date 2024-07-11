from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('Login', views.Login),
    path('Signup',views.Signup),
    path('index',views.index),
    path('newblog',views.newblog),
    path('post/<int:pk>',views.post, name ='post'),

]