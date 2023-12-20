from django.urls import path

from posts.views import (
    add_like,
    index,
    post_create,
    post_delete,
    post_edit,
    remove_like,
)

app_name = '%(app_label)s'

urlpatterns = [
    path(
        '',
        index,
        name='index',
    ),
    path(
        'create/',
        post_create,
        name='post_create',
    ),
    path(
        'posts/<int:pk>/edit/',
        post_edit,
        name='post_edit',
    ),
    path(
        'posts/<int:pk>/delete/',
        post_delete,
        name='post_delete',
    ),
    path(
        'posts/<int:pk>/add_like/',
        add_like,
        name='add_like',
    ),
    path(
        'posts/<int:pk>/remove_like/',
        remove_like,
        name='remove_like',
    ),
]
