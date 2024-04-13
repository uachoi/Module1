# editpw 앱의 urls.py 파일

from django.urls import path
from . import views

urlpatterns = [
    path('edit_password/<str:user_id>/', views.edit_password, name='edit_password'),
    path('change_password/<str:user_id>/', views.change_password, name='change_password'),
]
