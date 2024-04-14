from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from community import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include






urlpatterns = [
    path('', views.index),
    path('login.html', views.login_page, name='login'),
    path('my_page.html', views.my_page, name='my_page'),
    path('main.html', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('loginok.html', views.loginok_page, name='loginok'),
    path('logout.html/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_page2.html/', views.my_page2, name='my_page2'),
    path('community/create_post/', views.create_post, name='create_post'),
  

   

      

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)