import datetime as dt

from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    pub_date = serializers.DateTimeField(
        read_only=True, default=dt.datetime.now())

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    created = serializers.DateTimeField(
        read_only=True, default=dt.datetime.now())

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'created', 'post')
