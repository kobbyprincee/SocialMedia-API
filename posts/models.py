from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom User model
class User(AbstractUser):
    bio = models.TextField(max_length=250,blank=True,)
    profile_picture = models.ImageField('picture', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
    
#Custom Post model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.ImageField('picture', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

#Custom Comment Model 
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"

#Custom Like Model
class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Prevent Duplicate Likes
    class Meta:
        unique_together = ('user', 'post') 

    def __str__(self):
        return f"Post by {self.user.username} liked {self.post.title}"
