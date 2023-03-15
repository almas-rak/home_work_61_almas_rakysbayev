from django.views.generic import ListView, CreateView

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
    pass
