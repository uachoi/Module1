# mypage/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('delete/', views.delete_post, name='delete_post'),
]
