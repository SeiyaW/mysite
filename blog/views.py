from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog
from .forms import BlogCreateForm
from django.contrib import messages

# お知らせトップページ
class BlogIndexView(generic.TemplateView):
    template_name = 'blog_index.html'

    def get_context_data(self, **kwargs):
        blog = Blog.objects.order_by('-created_at')
        context = super().get_context_data()
        context['blog_list'] = blog
        return context

class BlogCreateView(generic.CreateView):
    model = Blog
    template_name = 'blog_create.html'
    form_class = BlogCreateForm
    success_url = reverse_lazy('blog:blog_index')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        messages.success(self.request, "ブログを作成しました。")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "ブログの作成に失敗しました。")
        return super().form_invalid(form)