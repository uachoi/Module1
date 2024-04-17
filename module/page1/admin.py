from django.contrib import admin
from .models import Post

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Post, QuestionAdmin)