from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.utils import paginate
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
