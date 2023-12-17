from django.urls import path

from posts.views import index

app_name = '%(app_label)s'

urlpatterns = [
    path(
        '',
        index,
        name='index',
    ),
]
