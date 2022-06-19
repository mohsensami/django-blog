from .models import Blog
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BlogCreateUpdateForm


def home(request):
    blogs = Blog.objects.all()
    stickies = Blog.objects.filter(sticky=True)
    return render(request, 'index.html', {'blogs': blogs, 'stickies': stickies})


def detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'detail.html', {'blog': blog})


def delete(request, id):
    Blog.objects.filter(id=id).delete()
    messages.success(request, 'article deleted successfully', 'success')
    return redirect('/')


def create(request):
    if request.method == 'POST':
        form = BlogCreateUpdateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Blog.objects.create(title=cd['title'], body=cd['body'], status=cd['status'], slug=cd['slug'])
            messages.success(request, 'article created successfully', 'success')
            return redirect('/')
    else:
        form = BlogCreateUpdateForm()
    return render(request, 'create.html', {'form': form})


def update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogCreateUpdateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'article updated successfully', 'success')
            return redirect('blog:detail', blog.id)
    else:
        form = BlogCreateUpdateForm(instance=blog)
    return render(request, 'update.html', {'form': form})

