from django.urls import path
from .views import (
    PersonListView,
    PersonDetailView,
    PersonCreateView,
    PersonUpdateView,
    PersonDeleteView,
)


app_name = "people"
urlpatterns = [
    path("", PersonListView.as_view(), name="list"),
    path("<slug:slug>/", PersonDetailView.as_view(), name="detail"),
    path("create/", PersonCreateView.as_view(), name="create"),
    path("<slug:slug>/update/", PersonUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", PersonDeleteView.as_view(), name="delete"),
]
