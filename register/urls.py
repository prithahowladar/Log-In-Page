from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name= "register"),
    path('info', views.userinfoview, name= "info"),
    path('thanks', views.thanks, name="thanks"),
]
