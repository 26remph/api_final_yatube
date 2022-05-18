from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers


class FollowSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username',
    )

    following = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Follow
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', )


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки постов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки групп."""
    class Meta:
        model = Group
        fields = '__all__'
