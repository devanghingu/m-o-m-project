from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path(instance,filename):
    return 'profileimage/user_{0}_{1}'.format(instance.user.id,filename)

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    bio         = models.TextField(blank=True,null=True)
    company     = models.CharField(max_length=35,blank=True,null=True)
    designation = models.CharField(max_length=25,blank=True,null=True)
    profile     = models.ImageField(upload_to=user_directory_path,default='profileimage/user_default.jpg')

    def __str__(self):
        return 'profile'