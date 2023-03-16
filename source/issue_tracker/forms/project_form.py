from django import forms

from issue_tracker.models import Project


class ProjectForm(forms.ModelForm):
    created_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    completed_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = ('name', 'description', 'created_at', 'completed_at')
        labels = {
            'name': 'Название проекта',
            'description': 'Описание',
            'created_at': 'Дата создания',
            'completed_at': 'Дата окончания',
        }
