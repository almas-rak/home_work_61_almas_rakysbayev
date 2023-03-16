from django import forms
from django.core.validators import BaseValidator, MinLengthValidator
from django.forms import CheckboxSelectMultiple

from issue_tracker.models import Task, Type


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=100):
        message = 'Максимальная длина  %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=CheckboxSelectMultiple,
        label='Тип'
    )

    summary = forms.CharField(
        validators=(MinLengthValidator(limit_value=5, message='Введите хотя бы 5 символов для названия'),
                    CustomLenValidator()))

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
