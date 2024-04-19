from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Posting,Comment,Category,Like
from django.contrib.auth.models import User

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

from django.http import JsonResponse

from django.urls import reverse
from django.db.models import Q


def index(request):
    return render(request, 'community/main_page.html')

def logout_view(request):
     logout(request)
     #return redirect('logout')
     return redirect('community')


@receiver(user_logged_out)       # 비회원 사용자
def on_user_logged_out(sender, request, user, **kwargs):
    return main_page(request)



def login_page(request):
    return render(request, 'community/login.html')

def my_page(request):   # 비회원으로 마이페이지접속할 때 
    #if request.method=='POST'
    
    return render(request,'community/my_page.html')


def main_page(request):     # 비회원 메인 페이지
    #posts = Posting.objects.all()       # 모든 게시글을 가져옴 --> related_name
    posts = Posting.objects.all().all().order_by('-pk')        #추가
    
    #category_id=request.POST.get('category')
    #category = Category.objects.get(pk=category_id)
    
    categories=Category.objects.all()
    return render(request, 'community/main_page.html',{'postings': posts,'categories':categories})



@login_required
def loginok_page(request):  # 로그인 상태의 메인페이지
     #posts = Posting.objects.all()      # 모든 게시글을 가져옴  - -> related_name
     posts = Posting.objects.all().all().order_by('-pk')        #추가
     
     categories=Category.objects.all()
     return render(request, 'community/loginok.html',{'postings': posts,'categories':categories})

@login_required
def my_page2(request):  # 회원일 때 마이페이지
    user = request.user
    return render(request, 'community/my_page2.html')


#def create_post(request):
    #return render(request, 'community/create_post.html')
    
@login_required
def create_post(request):
    author=request.user.username
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            category_id=request.POST.get('category')
            category = Category.objects.get(pk=category_id) 
            post = form.save(commit=False)  # 아직 저장하지 않음 // 저장 내용은 forms.py의 field 제목, 내용, 이미지
            post.tag=category
            post.created_at=timezone.now()    # 작성일자에 현재 시간 할당
            post.author = request.user.username     # 작성자 
            post.save()     # 이 때 저장
            
            #postings = Posting.objects.all()
        
            return redirect('loginok')  # 게시물 생성 후 메인 페이지로 리디렉션// return redirect('main_page')
            #return redirect(request,'loginok', {'postings': postings})   
    else:
        form = PostForm()
    categories=Category.objects.all()
    return render(request, 'community/create_post.html', {'form': form, 'categories':categories})


def post_detail(request, pk):       # 상세 페이지
    post = get_object_or_404(Posting, pk=pk)
    #postings = Posting.objects.get(pk=pk)
    post.views += 1
    post.save()
    likes_count = post.likes.count()
    
    comments=Comment.objects.filter(post=post)
    
    context = {
        'post': post,
        'comments': comments,
        'likes_count': likes_count, # 이 줄을 추가
    }
    
    return render(request, 'community/post_detail.html', context)
    #return render(request, 'community/post_detail.html',{'post': post,'comments': comments} )      ## {'posting': posting}


# 이미지 슬라이더
def img_view(request, pk):
    posting=Posting.objects.get(pk=pk)
    images=[posting.image1.url, posting.image2.url, posting.image3.url]
    
    context={
        'images':images
    }
    return render(request, 'community/post_detail.html', context)


# 검색기능 추가
def search_results(request):
    query = request.GET.get('q', '')  # 검색어를 'q' 파라미터로 가져옵니다.
    category_id=request.GET.get('category')        ## 검색에 카테고리 추가

    
    ## --------- 검색 조건 -------##
    if query:
        if category_id:
            # 검색어+카테고리
            category = Category.objects.get(pk=category_id)
            results = Posting.objects.filter(tag_id=category, title__icontains=query) | Posting.objects.filter(tag_id=category, content__icontains=query)
        else:
            #검색어만
            results = Posting.objects.filter(title__icontains=query) | Posting.objects.filter(content__icontains=query)
    elif category_id:
        # 카테고리만
        category = Category.objects.get(pk=category_id)
        results = Posting.objects.filter(category=category)
    else:
        # 검색어와 카테고리가 모두 없음
        results = Posting.objects.all()
        
    categories=Category.objects.all()

    # 검색 결과를 search_results.html 템플릿으로 렌더링합니다.
    return render(request, 'community/search_results.html', {'results': results, 'query': query, 'categories':categories})


#@receiver(user_logged_out)      ##### 비회원일 때 
def nonuser_post_detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    #postings = Posting.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    
    post.views += 1
    post.save()

    return render(request, 'community/nonuser_post_detail.html',{'post': post,'comments': comments} ) 

##  위의 코드 : board1에서 추가  ,,  community 앱과 모델, 필드명 맞춰서 수정


@login_required
def add_comment(request, pk):       # 댓글 남기기
    post = get_object_or_404(Posting, pk=pk)
    #postings = Posting.objects.all()
    #comments=Comment.objects.all()
    if request.method == "POST":
        ctext = request.POST.get('comment')
        comments=Comment.objects.create(post_id=pk, author=request.user, text=ctext)        ## request.user에서 수정
        comments.save()
        #return redirect('post_detail', {'postings': postings, 'comments':comments}, pk=post.pk)      # pk=pk 대신 {'post': post} 추가
        return redirect('post_detail', pk=post.pk)
    
def like_post(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created: # 이미 좋아요가 있다면 삭제
        like.delete()
        liked = False
    else:
        liked = True

    likes_count = post.count_likes()
    return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})
    

def post_delete(request, pk):   # 게시글 삭제
    post = get_object_or_404(Posting, pk=pk)
    post.delete()
    return redirect('loginok')        # 게시글을 삭제하면 메인화면으로


def post_edit(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'community/post_edit.html', {'form': form})

######^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^########

