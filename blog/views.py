from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def home(request):
    return HttpResponse('<h1>Blog</h1>')

