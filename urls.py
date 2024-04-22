from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from community import views
from .views import logout_view

#app_name = 'community'


urlpatterns = [
    path('', views.main_page),
    path('login.html', views.login_page, name='login'),
    path('my_page.html', views.my_page, name='my_page'),
    path('', views.main_page, name='community'),
    #path('main_page.html', auth_views.LogoutView.as_view(template_name='main_page.html'), name='main_page'),
    #path('main_page.html', auth_views.LogoutView.as_view(template_name='main_page.html'), name='main_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('loginok.html', views.loginok_page, name='loginok'),
    #path('logout.html/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_page2.html/', views.my_page2, name='my_page2'),
    path('community/create_post/', views.create_post, name='create_post'),
    path('logout/', logout_view, name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('community/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('community/post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    #path('community/post_detail/<int:pk>/', views.post_detail, name='post_detail'), # 각 게시물 상세 페이지로 넘어가도록
    #nonuser_post_detail
    path('community/post/<int:pk>/', views.nonuser_post_detail, name='nonuser_post_detail'),
    
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
    
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),

]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
