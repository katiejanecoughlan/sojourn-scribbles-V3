from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from cloudinary.models import CloudinaryField


class Profiles(models.Model):
    """
    Represents a user profile containing a bio and title.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    journal_title = models.CharField(max_length=200)
    profile_image = CloudinaryField(default='placeholder', folder='profile/', null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    bio = models.TextField(validators=[MaxLengthValidator(2000)])

    def __str__(self):
        return self.journal_title
