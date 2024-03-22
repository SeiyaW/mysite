from django.urls import path
from . import views

app_name = 'design'
urlpatterns = [
    path('', views.DesignIndexView.as_view(), name='design_index'),
]