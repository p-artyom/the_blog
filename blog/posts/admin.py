from django.contrib import admin

from core.admin import BaseAdmin
from posts.models import Like, Post, Topic


@admin.register(Topic)
class TopicAdmin(BaseAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display = (
        'pk',
        'content',
        'author',
        'created',
        'modified',
    )
    search_fields = ('content',)
    list_filter = ('created',)


@admin.register(Like)
class LikeAdmin(BaseAdmin):
    list_display = (
        'pk',
        'user',
        'post',
    )
