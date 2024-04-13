from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '가입이 완료되었습니다. 로그인해주세요.')
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})