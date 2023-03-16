from django.urls import path

from issue_tracker.views import IndexView, CreateTask, DetailTaskView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("create/task", CreateTask.as_view(), name='create_task'),
    path("detail/task/<int:pk>", DetailTaskView.as_view(), name='detail_task'),
]
