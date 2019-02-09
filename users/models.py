from django.db import models
from django.core.validators import URLValidator
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    fullname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=240, validators=[URLValidator()], blank=True, null=True)
    twitter = models.CharField(max_length=240, validators=[URLValidator()], blank=True, null=True)
    instagram = models.CharField(max_length=240, validators=[URLValidator()], blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

       

