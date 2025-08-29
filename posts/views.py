#Create views here
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from rest_framework import filters
# from django.shortcuts import get_object_or_404
from .models import Post, Like
from rest_framework import generics
from django.shortcuts import get_object_or_404
from notifications.models import Notification

#  Classes to implementation feeds for post of this social media app.

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        
        # Create notification for post author
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb='commented on your post',
                target=comment.post
            )
        
# --------------- #####################------------------------------#
#  Classes for the implementation of feeds for post of this social media app.
#----------------######################------------------------------#
class FeedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        feed_data = [
            {
                "id": post.id,
                "author": post.author.username,
                "content": post.content,
                "media": post.media,
                "created_at": post.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)
    


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # create a notification for the post's author
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor = request.user,
                    verb='liked your post',
                    target=post,
                )
            return Response({'message': 'Post liked successfuly!'})
        else:
            return Response({'message': 'you already liked this post.'}, status=400)
        
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully!'})
        else:
            return Response({'message': 'You have not liked this post yet.'}, status=400)
        
