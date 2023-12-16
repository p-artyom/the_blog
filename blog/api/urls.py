from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, TopicViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('topics', TopicViewSet, basename='topics')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
