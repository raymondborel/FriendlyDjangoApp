from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from .models import Post

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
class PostList(TemplateView):
    template_name = "post_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["posts"] = Post.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "All Posts"
        return context