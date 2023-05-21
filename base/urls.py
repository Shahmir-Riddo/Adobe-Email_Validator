
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/send-adobe-request/', views.index, name='index')
]
