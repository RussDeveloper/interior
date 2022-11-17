
from django.contrib import admin
from django.urls import path
from header.views import index


urlpatterns = [
    path('', index, name='home'),
]

