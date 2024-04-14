from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post





def index(request):
   
    return render(request, 'community/main.html')

def login_page(request):
    return render(request, 'community/login.html')

def my_page(request):
    
    return render(request,'community/my_page.html')

def main(request):
    posts = Post.objects.all()
    return render(request, 'community/main.html',{'posts': posts,})

def loginok_page(request):
     posts = Post.objects.all()
     return render(request, 'community/loginok.html',{'posts': posts,})


def my_page2(request):
    user = request.user
    return render(request, 'community/my_page2.html')


#def create_post(request):
    #return render(request, 'community/create_post.html')



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author_id = request.user.id 
            post.save()
            return redirect('main')  # 게시물 생성 후 메인 페이지로 리디렉션
    else:
        form = PostForm()
    return render(request, 'community/create_post.html', {'form': form})



