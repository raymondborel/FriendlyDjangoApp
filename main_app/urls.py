from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.PostList.as_view(), name="post_list"),
]
