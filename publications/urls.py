from django.urls import path
from .views import (
    PublicationListView,
    PublicationDetailView,
    PublicationCreateView,
    PublicationUpdateView,
    PublicationDeleteView,
)


app_name = "publication"
urlpatterns = [
    path("", PublicationListView.as_view(), name="list"),
    path("<slug:slug>/", PublicationDetailView.as_view(), name="detail"),
    path("create/", PublicationCreateView.as_view(), name="create"),
    path("<slug:slug>/update/", PublicationUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", PublicationDeleteView.as_view(), name="delete"),
]
