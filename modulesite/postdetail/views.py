# postdetail/views.py
from django.shortcuts import render

def post_detail(request, post_id):
    # 게시물 상세 정보를 가져오는 로직을 작성한다고 가정
    # post = Post.objects.get(id=post_id)
    # 상세 페이지 템플릿에 전달할 데이터를 가져온다고 가정
    # context = {'post': post}
    return render(request, 'postdetail/post_detail.html')
