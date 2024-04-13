from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def edit_password(request, user_id):
    return render(request, 'editpw/edit_password.html', {'user_id': user_id})

def change_password(request, user_id):
    error_message = None

    if request.method == 'POST':
        # 사용자가 입력한 기존 비밀번호와 새 비밀번호 가져오기
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        
        # 사용자 인증
        user = User.objects.get(username=user_id)
        if user.check_password(old_password):
            # 새 비밀번호로 변경
            user.set_password(new_password)
            user.save()
            return redirect('mypage')  # 비밀번호 변경 성공 페이지로 리다이렉트
        else:
            # 비밀번호가 일치하지 않을 때 에러 메시지 설정
            error_message = '기존 비밀번호가 일치하지 않습니다.'
    
    return render(request, 'editpw/edit_password.html', {'user_id': user_id, 'error_message': error_message})
