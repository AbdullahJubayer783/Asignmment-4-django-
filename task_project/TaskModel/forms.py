from django import forms
from .models import Task

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'taskTitle' : 'Task Title: ',
            'taskDescription' : 'Task Description: ',
            'is_completed' : 'Task is completed: '
        }
        widgets = {
            'Assign_Date' : forms.DateInput(attrs={'type' : 'date'})
        }

       