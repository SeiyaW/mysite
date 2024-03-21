from django.shortcuts import render
from django.views import generic

# Create your views here.
class NotificationIndexView(generic.TemplateView):
    template_name = 'notification_index.html'
