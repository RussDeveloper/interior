
from django.contrib import admin
from django.urls import path
from header.views import *


urlpatterns = [
    path('index/', index, name='home'),
    path('service/', service, name='service'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),
]

