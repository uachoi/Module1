from django.urls import path
from . import views

# app_name = 'module'

urlpatterns = [
    path('', views.index, name='index'),


]