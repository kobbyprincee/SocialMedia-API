# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Extend Django's AbstractUser with additional fields.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Many-to-Many relationship for followers
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        through="UserFollower",
        related_name="following",
    )


class UserFollower(models.Model):
    """
    Intermediate model to handle the followers relationship.
    """
    from_user = models.ForeignKey(CustomUser, related_name="following_set", on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name="follower_set", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')


    def __str__(self):
        return f"{self.from_user.username} follows {self.to_user.username}"
