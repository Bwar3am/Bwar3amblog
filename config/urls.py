from django.contrib import admin
from django.urls import path ,  include
from . import views
from .views import *


urlpatterns = [
    path("" , views.home , name='home' ),
    path("about/" , views.about , name="about"),
    path("content/<str:pk>" , views.content , name = "content")
]
