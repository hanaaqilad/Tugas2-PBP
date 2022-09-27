from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    class Meta:
        model = Task
        fields = ['title','description']
