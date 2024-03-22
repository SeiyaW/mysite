from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    path('', views.NotificationIndexView.as_view(), name='notification_index'),
    path('list/', views.NotificationListView.as_view(), name='notification_list'),
    path('detail/<int:pk>/', views.NotificationDetailView.as_view(), name='notification_detail'),
    path('create/', views.NotificationCreateView.as_view(), name='notification_create'),
]