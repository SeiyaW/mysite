from django.shortcuts import render
from django.views import generic
from notification.models import Notification
from blog.models import Blog

# Create your views here.
class DesignIndexView(generic.TemplateView):
    template_name = 'design_index.html'

    def get_context_data(self, **kwargs):
        notification = Notification.objects.order_by('-created_at')
        blog = Blog.objects.order_by('-created_at')
        context = super().get_context_data()
        context['notification_list'] = notification[0:3]
        context['blog_list'] = blog[0:3]
        return context

# デザイン制作用のページを作成
class DesignTestView(generic.TemplateView):
    template_name = 'design_test.html'

# デザイン2制作用のページを作成
class DesignTest2View(generic.TemplateView):
    template_name = 'design_test2.html'