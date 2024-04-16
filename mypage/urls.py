from django.urls import path
from . import views

app_name='mypage'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('delete/', views.delete_post, name='delete_post'),
    path('logout/', views.logout_view, name='logout'),
    path('mypage/',views.mypage, name='mypage'),
    
    #editpw 추가
    #path('edit_password/<str:user_id>/', views.edit_password, name='edit_password'),
    path('edit_password/<str:author>/', views.edit_password, name='edit_password'),
    path('change_password/<str:author>/', views.change_password, name='change_password'),
    
    #removeuser 추가
    path('remove_user/<str:author>/', views.remove_user, name='remove_user'),
    path('confirm_remove/<str:author>/', views.confirm_remove, name='confirm_remove'),
]