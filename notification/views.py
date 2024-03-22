from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Notification
from .forms import NotificationForm
from django.contrib import messages

# Create your views here.
# お知らせトップページ
class NotificationIndexView(generic.TemplateView):
    template_name = 'notification_index.html'

    def get_context_data(self, **kwargs):
        notification = Notification.objects.order_by('-created_at')
        context = super().get_context_data()
        context['notification'] = notification
        return context

# お知らせ作成ページ
class NotificationCreateView(generic.CreateView):
    model = Notification
    template_name = 'notification_create.html'
    form_class = NotificationForm
    success_url = reverse_lazy('notification:notification_index')

    def form_valid(self, form):
        notification = form.save(commit=False)
        notification.save()
        messages.success(self.request, "お知らせを作成しました。")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "お知らせの作成に失敗しました。")
        return super().form_invalid(form)

# お知らせ一覧
class NotificationListView(generic.ListView):
    model = Notification
    template_name = 'notification_list.html'
    paginate_by = 10

    def get_queryset(self):
        notification = Notification.objects.order_by('-created_at')
        return notification

# お知らせ詳細
class NotificationDetailView(generic.DetailView):
    model = Notification
    template_name = 'notification_detail.html'