from .models import Blog
from django.shortcuts import render


def home(request):
    blogs = Blog.objects.all()
    stickies = Blog.objects.filter(sticky=True)
    return render(request, 'index.html', {'blogs': blogs, 'stickies': stickies})
