from django.contrib import admin
from .models import Notification

# Register your models here.
# Django管理画面でDB操作できるようにするための設定
admin.site.register(Notification)