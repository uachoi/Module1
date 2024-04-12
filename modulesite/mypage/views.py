# views.py

from django.shortcuts import render, redirect
from .models import Post

def mypage(request):
    # user_id가 "test"인 데이터를 가져옴
    posts = Post.objects.filter(user_id='test', is_del=False)
    return render(request, 'mypage/mypage.html', {'posts': posts})

def delete_post(request):
    if request.method == 'POST':
        post_ids = request.POST.getlist('post_ids')  # 체크된 행의 ID 목록 가져오기
        # 각 체크된 행의 is_del 값을 True로 업데이트
        Post.objects.filter(id__in=post_ids).update(is_del=True)
    return redirect('mypage')  # my_page 뷰로 리다이렉트

