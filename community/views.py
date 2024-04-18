from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Posting,Comment,Category
from django.contrib.auth.models import User

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

from django.http import JsonResponse

from django.urls import reverse
from django.db.models import Q

def index(request):
    return render(request, 'community/main_page.html')

def login_page(request):
    return render(request, 'community/login.html')

def my_page(request):   # 비회원으로 마이페이지접속할 때 
    return render(request,'community/my_page.html')

@receiver(user_logged_out)       # 비회원 사용자
def on_user_logged_out(sender, request, user, **kwargs):
    return main_page(request)

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

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    #postings = Posting.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    
    post.views += 1
    post.save()
    return render(request, 'community/post_detail.html',{'post': post,'comments': comments} )      ## {'posting': posting}

# 검색기능 추가
def search_results(request):
    query = request.GET.get('q', '')  # 검색어를 'q' 파라미터로 가져옵니다.
    
    category_id=request.GET.get('category')        ## 검색에 카테고리 추가
    #category = Category.objects.get(id)     ## 검색에 카테고리 추가
    #category_id=request.GET.get('category')        ## 검색에 카테고리 추가
    
    ## --------- 검색 조건 -------##
    if query:
        # 검색어가 있을 때
        if category_id:
            # 검색어+카테고리
            category = Category.objects.get(pk=category_id)
            results = Posting.objects.filter(category=category, title__icontains=query) | Posting.objects.filter(category=category, content__icontains=query)
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
    
    # if query:
    #     results = Posting.objects.filter(title__icontains=query) | Posting.objects.filter(content__icontains=query) 
        
    # # 카테고리가 선택되었는지
    # if category_id:
    #     try:
    #         category = Category.objects.get(pk=category_id)     ## 선택된 카테고리 객체 추가
    #         results = results.filter(tag=category) 
    #         #Posting.objects.filter(category=category,content__icontains=query)
    #     except Category.DoesNotExist:
    #         pass
    # #else:
    # #    results = []
        
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
	post = get_object_or_404(Posting, id=pk)       # pk=pk
	# if post.likes.filter(id=request.user.id).exists():
	# 	post.likes.remove(request.user)
	# 	liked = False
	# else:
	# 	post.likes.add(request.user)
    
	# 	liked = True
	# return JsonResponse({'liked': liked, 'likes': post.likes.count()})
 
    #post.likes += 1
    #post.save()
    
    
    ##  위의 코드 : board1에서 추가  ,,  community 앱과 모델, 필드명 맞춰서 수정
    
    
    ## 밑에 코드들은 마이페이지에 해당하는 뷰 함수

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
            return redirect('boards1:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'boards1/post_edit.html', {'form': form})

######^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^########

