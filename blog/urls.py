from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog_index'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
]