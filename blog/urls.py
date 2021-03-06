from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
]
