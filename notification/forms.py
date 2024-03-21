from .models import Notification
from django import forms

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'