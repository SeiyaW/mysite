from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog_index'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
]