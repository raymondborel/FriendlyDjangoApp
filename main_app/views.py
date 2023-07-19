from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from django import forms
from .models import Post, Category, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
@method_decorator(login_required, name='dispatch')
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
    
# class CategoryList(TemplateView):
#     template_name = "category_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get("name")
#         if name != None:
#             context["categorys"] = Category.objects.filter(name__icontains=name)
#             context["header"] = f"Searching for {name}"
#         else:
#             context["categorys"] = Category.objects.all()
#             context["header"] = "All Posts"
#         return context
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'img', 'body']
    
    category = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        choice_list = kwargs.pop('choice_list', None)
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Select a category')] + choice_list

@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = "category_create.html"
    def get_success_url(self):
        return reverse('post_create')

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super(PostCreate, self).get_form_kwargs()
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = [(item[0], item[0]) for item in choices]
        kwargs['choice_list'] = choice_list
        return kwargs

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'img', 'body']
    template_name = "post_update.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    
class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = "/posts/"

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['bio', 'profile_img', 'social_link']
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

class ProfileCreate(CreateView, LoginRequiredMixin):
    model = Profile
    fields = ['bio', 'profile_img', 'social_link']
    template_name = "profile_create.html"

    def form_valid(self, form):
        # Set the user before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})



class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_create")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
