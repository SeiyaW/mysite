from django.urls import path
from . import views

app_name = 'design'
urlpatterns = [
    path('', views.DesignIndexView.as_view(), name='design_index'),
    path('test/', views.DesignTestView.as_view(), name='design_test'),
    path('test2/', views.DesignTest2View.as_view(), name='design_test2'),
]