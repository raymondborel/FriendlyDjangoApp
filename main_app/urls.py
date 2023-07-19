from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('categories/new/', views.CategoryCreate.as_view(), name="category_create"),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update',views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete',views.PostDelete.as_view(), name="post_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profiles/new/', views.ProfileCreate.as_view(), name="profile_create"),
]
