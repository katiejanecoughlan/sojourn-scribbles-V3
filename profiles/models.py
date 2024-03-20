from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profiles(models.Model):
    """
    Represents a user profile containing a bio, title, profile image, and post content.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
