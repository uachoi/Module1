from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Posting,Comment,Category, Like
from django.contrib.auth.models import User

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

from django.http import JsonResponse
from django.contrib import messages

#from page1.models import Profile

def index(request):
    return render(request, 'community/main_page.html')

def login_page(request):
    return render(request, 'community/login.html')

def my_page(request):   # 비회원으로 마이페이지접속할 때 
    return render(request,'community/my_page.html')

def logout_view(request):
    logout(request)
    return redirect('community')
    
@receiver(user_logged_out)       # 비회원 사용자
def on_user_logged_out(sender, request, user, **kwargs):
    return main_page(request)

def main_page(request):     # 비회원 메인 페이지
    posts = Posting.objects.all().all().order_by('-pk')       # 모든 게시글을 가져옴 --> related_name
    return render(request, 'community/main_page.html',{'postings': posts,})

@login_required
def loginok_page(request):  # 로그인 상태의 메인페이지
     posts = Posting.objects.all()      # 모든 게시글을 가져옴  - -> related_name
     return render(request, 'community/loginok.html',{'postings': posts,})

@login_required
def my_page2(request):  # 회원일 때 마이페이지
    user = request.user
    return render(request, 'community/my_page2.html')


#def create_post(request):
    #return render(request, 'community/create_post.html')

def post_detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    #postings = Posting.objects.get(pk=pk)
    post.views += 1
    post.save()
    likes_count = post.likes.count()

    comments=Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'likes_count': likes_count,  # 이 줄을 추가
    }
    
    return render(request, 'community/post_detail.html', context)      ## {'posting': posting}

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
        
            return redirect('loginok')  # 게시물 생성 후 메인 페이지로 리디렉션// return redirect('main')
            #return redirect(request,'loginok', {'postings': postings})   
    else:
        form = PostForm()
    categories=Category.objects.all()
    return render(request, 'community/create_post.html', {'form': form, 'categories':categories})

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
    
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Posting, pk=comment.post.pk)  # 댓글이 속한 게시글

    # 댓글 작성자 또는 게시글 작성자인 경우 삭제 가능
    if request.user == comment.author or request.user.username == post.author:
        comment.delete()
        messages.success(request, '댓글이 삭제되었습니다.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        messages.error(request, '댓글을 삭제할 권한이 없습니다.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
#def like_post(request, pk):
	#post = get_object_or_404(Posting, id=pk)       # pk=pk
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
#@login_required
#def like_post(request, pk):
#    post = get_object_or_404(Posting, pk=pk)
#    post.likes += 1  # 좋아요 수 증가
#    post.save()
#    return JsonResponse({'likes': post.likes})  # 업데이트된 좋아요 수를 JSON 응답으로 반환    
    
    ## 밑에 코드들은 마이페이지에 해당하는 뷰 함수
@login_required
def like_post(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:  # 이미 좋아요가 있다면 삭제
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


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Posting, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user.username  # 필요한 경우, 작성자 정보를 갱신합니다.
            updated_post.save()
            # 성공 메시지를 추가하는 것을 고려할 수 있습니다.
            # messages.success(request, '게시글이 성공적으로 수정되었습니다.')
            return redirect('post_detail', pk=updated_post.pk)  # 게시글 상세 페이지로 리디렉션
    else:
        form = PostForm(instance=post)

    return render(request, 'community/post_edit.html', {'form': form, 'post': post})

######^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^########

