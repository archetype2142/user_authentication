from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE) # ?
    protfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username
    