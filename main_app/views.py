from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    