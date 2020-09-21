from django import forms
from django.forms import ModelForm
from .models import *

class Taskform(forms.ModelForm):

    class Meta:
        model = task
        fields = '__all__'
