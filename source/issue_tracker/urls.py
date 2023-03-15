from django.urls import path

from issue_tracker.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]
