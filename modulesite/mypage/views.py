# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 추가
from .models import Post
from django.contrib.auth import logout

@login_required
def mypage(request):
    user_id = request.user.username
    # user_id가 "test"인 데이터를 가져옴
    posts = Post.objects.filter(user_id=user_id, is_del=False)
    return render(request, 'mypage/mypage.html', {'user_id': user_id, 'posts': posts})

def delete_post(request):
    if request.method == 'POST':
        post_ids = request.POST.getlist('post_ids')  # 체크된 행의 ID 목록 가져오기
        # 각 체크된 행의 is_del 값을 True로 업데이트
        Post.objects.filter(id__in=post_ids).update(is_del=True)
    return redirect('mypage')  # my_page 뷰로 리다이렉트


def logout_view(request):
    logout(request)
    return redirect('login')  # 로그아웃 후 로그인 페이지로 리다이렉트