# removeuser 앱의 urls.py 파일

from django.urls import path
from . import views

urlpatterns = [
    path('remove_user/<str:user_id>/', views.remove_user, name='remove_user'),
    path('confirm_remove/<str:user_id>/', views.confirm_remove, name='confirm_remove'),
]
