from django.db import models
from django.utils import timezone
#from page1.models import Profile

# class MyPost(models.Model):
#     subject = models.CharField(max_length=100)      ## 제목
#     tag = models.CharField(max_length=50)       ## category
#     view_count = models.IntegerField()      ## 조회수
#     post_create_time = models.DateTimeField(default=timezone.now)
    
#     # 사용자 ID 추가 - -> 앱 page1의 Profile의 user
#     #user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='mypost')
    
#     is_del = models.BooleanField(default=False) # 삭제 플래그

#     def __str__(self):
#         return self.subject
    
#     class Meta:
#         db_table='mypost'