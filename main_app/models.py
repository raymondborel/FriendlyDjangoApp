from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=300)
    social_link = models.CharField(max_length=200, default="@nulll")

    def __str__(self):
        return str(self.user)