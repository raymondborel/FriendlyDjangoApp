from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']