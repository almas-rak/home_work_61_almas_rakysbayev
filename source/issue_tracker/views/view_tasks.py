from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from issue_tracker.forms.task_form import TaskForm
from issue_tracker.models import Task


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset


class CreateTask(CreateView):
    template_name = 'create_task.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class DetailTaskView(DetailView):
    template_name = 'detail_task.html'
    model = Task
