from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image1' ,'image2' ,'image3']

# 검색기능 추가
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

