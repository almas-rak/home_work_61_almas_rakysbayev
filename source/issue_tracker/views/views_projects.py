from django.views.generic import ListView

from issue_tracker.models import Project


class ListProjectView(ListView):
    template_name = 'projects_templates/list_projects.html'
    model = Project
    context_object_name = 'projects'
    ordering = 'created_at'

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset
