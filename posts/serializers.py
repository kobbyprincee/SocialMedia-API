from rest_framework import serializers
from .models import User,Post,Comment,Like

#Creaate Serializers Here

#Serializer for User Model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'post', 'post_title', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Like
        fields = ['id', 'author', 'post', 'post_title', 'created_at', 'updated_at']