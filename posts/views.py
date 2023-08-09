from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class HomePageView(ListView):
    model = Post
    template_name ='home_p.html'
    context_object_name = 'all_post_list'
