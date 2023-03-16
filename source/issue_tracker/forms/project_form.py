from django import forms

from issue_tracker.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created_at', 'completed_at')
        labels = {
            'name': 'Название проекта',
            'description': 'Описание',
            'created_at': 'Дата создания',
            'completed_at': 'Дата окончания',
        }
