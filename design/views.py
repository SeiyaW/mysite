from django.shortcuts import render
from django.views import generic
from notification.models import Notification
from blog.models import Blog

# Create your views here.
class DesignIndexView(generic.TemplateView):
    template_name = 'design_index.html'

    def get_context_data(self, **kwargs):
        notification = Notification.objects.order_by('-created_at')
        blog = Blog.objects.order_by('created_at')
        context = super().get_context_data()
        context['notification_list'] = notification
        context['blog_list'] = blog
        return context

# デザイン制作用のページを作成
class DesignTestView(generic.TemplateView):
    template_name = 'design_test.html'