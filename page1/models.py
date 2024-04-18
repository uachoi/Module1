from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import Profile
from community.models import Posting
# 클래스는 각 테이블
 

class Post(models.Model):       # 테이블명이 modlue_post로 들어감
    subject = models.CharField(max_length=200)  #id
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    
    class Meta:
        db_table='listuser'
    
class Answer(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    
# class Profile(models.Model):    # auth_user에서 UK로 설정된 username을 ㄱ사용하기 위한 모델
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
#     def __str__(self):
#         return self.user.username
    
#     class Meta:
#         db_table='profile'
        
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)       # 사용자 프로필 생성
#         Posting.objects.create(user=instance)       # 사용자 게시물 생성