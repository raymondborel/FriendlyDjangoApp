from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('users/', views.UserList.as_view(), name="user_list"),
]
