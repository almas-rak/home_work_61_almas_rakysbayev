from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from issue_tracker.forms import ProjectForm, ProjectTaskForm
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
        tasks = Task.objects.filter(project=project, is_deleted=False).select_related('status').prefetch_related(
            'type')
        context['tasks'] = tasks
        return context


class CreateProjectView(CreateView):
    template_name = 'projects_templates/create_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class CreateProjectTaskView(CreateView):
    template_name = 'projects_templates/create_project_task.html'
    model = Task
    form_class = ProjectTaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('pk')
        project = Project.objects.get(id=project_id)
        context['project'] = project
        return context

    def form_valid(self, form):
        project_id = self.kwargs.get('pk')
        project = Project.objects.get(id=project_id)
        form.instance.project = project
        return super().form_valid(form)

    def get_initial(self):
        project_id = self.kwargs.get('pk')
        project = Project.objects.get(id=project_id)
        return {'project': project}

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('detail_project', kwargs={'pk': pk})


class DetailProjectTaskView(DetailView):
    template_name = 'tasks_templates/detail_task.html'
    model = Task


class DeleteProjectTaskView(DeleteView):
    pass
