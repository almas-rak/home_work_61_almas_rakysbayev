from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from issue_tracker.forms import TaskForm
from issue_tracker.models import Task, Status, Type, Project


def create(request):
    count = 4
    status = Status.objects.filter(id=1)
    status = status[0]
    t = Type.objects.filter(id=3)
    project = Project.objects.filter(id=1)
    project = project[0]

    for i in range(20):
        count += 1
        task = Task(summary=f'Тест {count}', description='тест страниц', status=status, project=project)
        task.save()
        task.type.set(t)
    reverse('index')


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset


class CreateTask(CreateView):
    template_name = 'tasks_templates/create_task.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class UpdateTaskView(UpdateView):
    template_name = 'tasks_templates/update_task.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class DetailTaskView(DetailView):
    template_name = 'tasks_templates/detail_task.html'
    model = Task


class DeleteTaskView(DeleteView):
    template_name = 'tasks_templates/detail_task.html'
    model = Task
    extra_context = {'delete': 'delete'}
    success_url = reverse_lazy('index')
