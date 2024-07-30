from django.urls import path
from . import views

app_name = "responsible_computing"
urlpatterns = [
    path("", views.index, name="responsible_computing"),
]
