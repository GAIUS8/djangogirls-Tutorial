from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    # posts 변수에 ORM을 이용해서 전체 Post의 리스트를 대입
    # posts 변수에 ORM을 이용해서 published_date timezone을 이용하여 최근 이전에 퍼블리쉬된 글들만 전달
    posts = Post.objects.filter(published_date__lte=timezone.now())
    print(posts)
    context = {
        'title': 'PostList from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)
