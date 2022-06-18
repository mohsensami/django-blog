from .models import Blog
from django.shortcuts import render


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})
