from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from community import views

#app_name = 'community'


urlpatterns = [
    path('', views.index),
    path('login.html', views.login_page, name='login'),
    path('my_page.html', views.my_page, name='my_page'),
    path('main_page.html', views.main_page, name='main_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('loginok.html', views.loginok_page, name='loginok'),
    path('logout.html/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_page2.html/', views.my_page2, name='my_page2'),
    path('community/create_post/', views.create_post, name='create_post'),
    
    path('community/post_detail/<int:pk>/', views.post_detail, name='post_detail'), # 각 게시물 상세 페이지로 넘어가도록
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
    
    path('like_post/<int:pk>/', views.like_post, name='like_post'),



]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)