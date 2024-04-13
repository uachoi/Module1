# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def remove_user(request, user_id):
    return render(request, 'removeuser/remove_user.html', {'user_id': user_id})

def confirm_remove(request, user_id):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = User.objects.get(username=user_id)
        if user.check_password(password):
            # 비밀번호 검증 성공 시 회원 탈퇴
            user.delete()
            return redirect('login')  # 성공 페이지로 리다이렉트
        else:
            # 비밀번호가 일치하지 않을 때 에러 메시지 설정
            error_message = '비밀번호가 일치하지 않습니다.'
    
    return render(request, 'removeuser/remove_user.html', {'user_id': user_id, 'error_message': error_message})
        