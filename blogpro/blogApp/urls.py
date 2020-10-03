
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('addUser',v.addUser),
    path('mylogin',v.mylogin),
    path('logOUT',v.logOUT),
    path('myblog',v.myblog),
    path('beaches',v.beaches),
    path('fort',v.fort),
    path('hill',v.hill),
    

]