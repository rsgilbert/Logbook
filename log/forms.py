from django import forms
from .models import Log
from django.forms import ModelForm, Textarea

class LogModelForm(ModelForm):
    class Meta:
        model = Log
        fields = ['day', 'activities', 'plans']
        widgets = {
         'activities': Textarea(),
         'plans': Textarea()
        }