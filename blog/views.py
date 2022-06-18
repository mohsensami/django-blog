from .models import Blog
from django.shortcuts import render


def home(request):
    blogs = Blog.objects.all()
    stickies = Blog.objects.filter(sticky=True)
    return render(request, 'index.html', {'blogs': blogs, 'stickies': stickies})


def detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'detail.html', {'blog': blog})