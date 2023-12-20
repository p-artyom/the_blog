from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from core.utils import paginate
from posts.forms import PostForm
from posts.models import Like, Post


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'posts/index.html',
        {
            'page_obj': paginate(
                request,
                Post.objects.select_related('author'),
            ),
            'like': Like.objects.values('post').annotate(
                count_like=Count('post'),
            ),
        },
    )


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    form = PostForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(
            request,
            'posts/create_post.html',
            {
                'form': form,
            },
        )
    form.instance.author = request.user
    form.save()
    return redirect('posts:index')


@login_required
def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('posts:index')
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post,
    )
    if not form.is_valid():
        return render(
            request,
            'posts/create_post.html',
            {
                'form': form,
                'is_edit': True,
            },
        )
    form.save()
    return redirect('posts:index')


@login_required
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('posts:index')
    post.delete()
    return redirect('posts:index')


@login_required
def add_like(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    Like.objects.create(user=request.user, post=post)
    return redirect('posts:index')


@login_required
def remove_like(request: HttpRequest, pk: int) -> HttpResponse:
    like = get_object_or_404(Like, user=request.user, post=pk)
    like.delete()
    return redirect('posts:index')
