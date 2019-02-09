from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from marketing.models import Signup

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        print('here')
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-timestamp'][0:3]


def post(request):
    return render(request, 'post.html', {})