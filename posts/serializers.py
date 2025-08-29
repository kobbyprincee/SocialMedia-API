from rest_framework import serializers
from .models import Post,Comment,Like

#Creaate Serializers Here

#Serializer for User Model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'content', 'media', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'post', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']