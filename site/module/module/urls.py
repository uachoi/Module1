from django.urls import path
from . import views   
from django.contrib.auth import views as auth_views

app_name = 'module'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='module/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
]