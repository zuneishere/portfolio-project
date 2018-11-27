from django.contrib import admin
from django.urls import path

import blogs.views

urlpatterns = [
    path('',blogs.views.allblogs,name='allblogs'),
    path('<int:blogid>/',blogs.views.detail,name='details')
]
