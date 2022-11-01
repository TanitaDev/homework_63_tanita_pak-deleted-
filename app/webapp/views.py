from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import PostForm
from webapp.models import Post


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = "add_post.html"
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('index')
