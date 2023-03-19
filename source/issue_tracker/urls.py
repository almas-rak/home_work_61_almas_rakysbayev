from django.urls import path

from issue_tracker.views import IndexView, CreateTask, DetailTaskView, DeleteTaskView, UpdateTaskView, ListProjectView, \
    DetailProjectView, CreateProjectView, CreateProjectTaskView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("create/task", CreateTask.as_view(), name='create_task'),
    path("detail/task/<int:pk>", DetailTaskView.as_view(), name='detail_task'),
    path("delete/task/<int:pk>", DeleteTaskView.as_view(), name='delete_task'),
    path("update/task/<int:pk>", UpdateTaskView.as_view(), name='update_task'),
    path("list/projects/", ListProjectView.as_view(), name='list_projects'),
    path("detail/projects/<int:pk>", DetailProjectView.as_view(), name='detail_project'),
    path("create/project", CreateProjectView.as_view(), name='create_project'),
    path("create/project/task/<int:pk>", CreateProjectTaskView.as_view(), name='create_project_task'),
    path("detail/project/task/<int:task>/<int:project>", CreateProjectTaskView.as_view(),
         name='detail_project_task_view'),
]
