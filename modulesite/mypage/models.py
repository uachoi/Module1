# models.py

from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    view_count = models.IntegerField()
    post_create_time = models.DateTimeField()
    user_id = models.CharField(max_length=50)  # 사용자 ID 추가
    is_del = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
