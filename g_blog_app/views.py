from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.

#index Page

class indexPage(ListView):
    model = Post 
    template_name = 'folder/index.html'
    context_object_name = 'posts'
    
# class detailPage(DetailView):
#     model = Post
#     context_object_name = 'post'
#     template_name = 'folder/detailpage.html'
    
#     def def get_queryset(self):
#         return Post.objects.exclude(slug)

def detailPage(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.exclude(slug=slug)[:3] 
    context = {
        'post':post,
        'posts': posts,
        # 'categories':categories,
    }
    return render(request, 'folder/detailpage.html', context)