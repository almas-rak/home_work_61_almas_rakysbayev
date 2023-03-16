from django.urls import path

from issue_tracker.views import IndexView, CreateTask, DetailTaskView, DeleteTaskView, UpdateTaskView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("create/task", CreateTask.as_view(), name='create_task'),
    path("detail/task/<int:pk>", DetailTaskView.as_view(), name='detail_task'),
    path("delete/task/<int:pk>", DeleteTaskView.as_view(), name='delete_task'),
    path("update/task/<int:pk>", UpdateTaskView.as_view(), name='update_task'),

]
