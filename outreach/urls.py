from django.urls import path
from . import views

app_name = "outreach"
urlpatterns = [
    path("", views.index, name="outreach"),
]
