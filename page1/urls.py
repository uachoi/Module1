from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'page1'

urlpatterns = [
    path('', views.index, name='index'),
    path('', auth_views.LogoutView.as_view(template_name='main_page.html')),
    
    

]