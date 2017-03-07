from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

from taskmanagement.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'difficulty',
            'due_date',
            'assignee',
        ]
        widgets = {
            'due_date': SelectDateWidget(),
        }
