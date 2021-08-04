from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, default="")
    bio = models.TextField()
    followers = models.ManyToManyField(User,related_name="followers", blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)


    def __str__(self):
        return f'Profile for user {self.user.username}'

    def get_absolute_url(self):
        return reverse('user_profile', args=[self.id])