from django.contrib import admin
from .models import Post, Profile, Category, City
# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(City)