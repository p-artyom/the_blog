from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from posts.models import Like, Post, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    number_likes = serializers.SerializerMethodField()
    topic = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Topic.objects.all(),
        many=True,
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'number_likes', 'created', 'modified')

    @extend_schema_field({'example': 0})
    def get_number_likes(self, object):
        review = Like.objects.filter(post=object.id)
        if review.exists():
            return review.count()
        return 0


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, data):
        if Like.objects.filter(
            user=self.context.get('request').user,
            post=data['post'],
        ).exists():
            raise serializers.ValidationError(
                {'errors': 'Вы уже поставили лайк этому посту!'},
            )
        return data
