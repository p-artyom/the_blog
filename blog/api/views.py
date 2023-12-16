from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.permissions import AuthorCanEditAndDelete
from api.serializers import LikeSerializer, PostSerializer, TopicSerializer
from posts.models import Like, Post, Topic


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        AuthorCanEditAndDelete,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=['POST'],
    )
    def add_like(self, request, pk):
        '''Поставить лайк.'''

        data = {'user': request.user.id, 'post': pk}
        serializer = LikeSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=['POST'],
    )
    def remove_like(self, request, pk):
        '''Удалить лайк.'''

        try:
            like = Like.objects.get(user=request.user, post=pk)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(
                {'errors': 'Вы не ставили лайк данному посту!'},
                status=status.HTTP_400_BAD_REQUEST,
            )
