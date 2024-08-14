from django.urls import path
from .views import (
    RobotListView,
    RobotDetailView,
    RobotCreateView,
    RobotUpdateView,
    RobotDeleteView,
)


app_name = "robots"
urlpatterns = [
    path("", RobotListView.as_view(), name="list"),
    path("<slug:slug>/", RobotDetailView.as_view(), name="detail"),
    # path("create/", RobotCreateView.as_view(), name="create"),
    # path("<slug:slug>/update/", RobotUpdateView.as_view(), name="update"),
    # path("<slug:slug>/delete/", RobotDeleteView.as_view(), name="delete"),
]
