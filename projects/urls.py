from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)


app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="detail"),
    path("create/", ProjectCreateView.as_view(), name="create"),
    path("<slug:slug>/update/", ProjectUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", ProjectDeleteView.as_view(), name="delete"),
]
