from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 추가
#from .models import MyPost
from django.contrib.auth import logout

from community.models import Posting ## Post 앱의 모델을 사용

#editpw 추가
from django.contrib.auth.models import User
from django.contrib import messages

def edit_password(request, author):        # author => username
    #user = Posting.objects.get(username=username)    # add
    return render(request, 'mypage/edit_password.html', {'author': author})

def change_password(request, author):
    error_message = None
    #user = Posting.objects.get(username=username)    # add

    if request.method == 'POST':
        # 사용자가 입력한 기존 비밀번호와 새 비밀번호 가져오기
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        
        # 사용자 인증
        user = User.objects.get(username=author)
        if user.check_password(old_password):
            # 새 비밀번호로 변경
            user.set_password(new_password)
            user.save()
            return redirect('mypage')  # 비밀번호 변경 성공 페이지로 리다이렉트
        else:
            # 비밀번호가 일치하지 않을 때 에러 메시지 설정
            error_message = '기존 비밀번호가 일치하지 않습니다.'
    
    return render(request, 'mypage/edit_password.html', {'author': author, 'error_message': error_message})
##==============================##

## removeuser 추가
def remove_user(request, author):
    #user = Posting.objects.get(username=username)    # add
    
    return render(request, 'mypage/remove_user.html', {'author': author})

def confirm_remove(request, author):
    #user = Posting.objects.get(username=username)    # add
    if request.method == 'POST':
        password = request.POST.get('password')
        user = Posting.objects.get(username=author)
        if user.check_password(password):
            # 비밀번호 검증 성공 시 회원 탈퇴
            user.delete()
            return redirect('common:login')  # 성공// 로그인 페이지로 리다이렉트
        else:
            # 비밀번호가 일치하지 않을 때 에러 메시지 설정
            error_message = '비밀번호가 일치하지 않습니다.'
    
    return render(request, 'mypage/remove_user.html', {'author': author, 'error_message': error_message})

##==============================##

@login_required
def mypage(request):
    author = request.user.username
    # author가 "test"인 데이터를 가져옴
    posts = Posting.objects.filter(author=author, is_del=False)      #author=author
    return render(request, 'mypage/mypage.html', {'author': author, 'posts': posts})

def delete_post(request):
    if request.method == 'POST':
        post_ids = request.POST.getlist('post_ids')  # 체크된 행의 ID 목록 가져오기
        # 각 체크된 행의 is_del 값을 True로 업데이트
        Posting.objects.filter(id__in=post_ids).update(is_del=True)
    return redirect('mypage')  # my_page 뷰로 리다이렉트


def logout_view(request):
    logout(request)
    return redirect('common:login')  # 로그아웃 후 로그인 페이지로 리다이렉트