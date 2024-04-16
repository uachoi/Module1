from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from page1.models import Profile

from django.conf import settings
#from page1.models import auth_user

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        db_table='category'

class Posting(models.Model):    # 게시글 작성 모델
    post_id = models.AutoField(primary_key=True)    #고유 식별 ID
    title = models.CharField(max_length=100)    
    content = models.TextField()
    
    # 작성자(=가입 시 사용한 사용자 아이디)
    author=models.CharField(max_length=50)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='posting_auth')  # author 필드를 ForeignKey로 설정
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    #likes = models.ManyToManyField(User, related_name='posting_like')
    comments = models.IntegerField(default=0)
    
    image1 = models.ImageField(upload_to='community/uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='community/uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='community/uploads/', blank=True, null=True)
    
    tag=models.ForeignKey(Category, on_delete=models.CASCADE, default='', related_name='posting_tag')
    is_del=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    class Meta:
        db_table = 'posting'
        
        
class Comment(models.Model):
    post = models.ForeignKey('Posting', on_delete=models.CASCADE, related_name='post_comment')
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)    
    
    # def save(self, *args, **kwargs):
    #     # author 필드에는 사용자 객체(User)의 username이 아닌 사용자 객체(User)를 직접 할당해야 합니다.
    #     # 예를 들어, 현재 로그인된 사용자를 할당할 수 있습니다.
    #     self.author = User.objects.get(username='사용자이름')
    #     super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'comment'