from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# お知らせトップページ
class BlogIndexView(generic.TemplateView):
    template_name = 'blog_index.html'
