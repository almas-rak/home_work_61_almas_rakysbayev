from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from issue_tracker.forms import ProjectForm
from issue_tracker.models import Project, Task


class ListProjectView(ListView):
    template_name = 'projects_templates/list_projects.html'
    model = Project
    context_object_name = 'projects'
    ordering = 'created_at'

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset


class DetailProjectView(DetailView):
    template_name = 'projects_templates/detail_project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        tasks = Task.objects.filter(project=project, is_deleted=False)
        context['tasks'] = tasks
        return context


class CreateProjectView(CreateView):
    template_name = 'projects_templates/create_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})

