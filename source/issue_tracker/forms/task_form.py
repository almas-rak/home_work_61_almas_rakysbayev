from django import forms
from django.forms import CheckboxSelectMultiple

from issue_tracker.models import Task, Type


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=CheckboxSelectMultiple,
        label='Тип'
    )

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type', 'project')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'type': 'Тип',
            'project': 'Проект',
        }
