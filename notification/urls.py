from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    path('', views.NotificationIndexView.as_view(), name='notification_index'),
    path('create/', views.NotificationCreateView.as_view(), name='notification_create'),
]