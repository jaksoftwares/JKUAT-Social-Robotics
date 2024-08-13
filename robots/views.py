from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Robot


class RobotListView(ListView):
    model = Robot
    template_name = "robots/list.html"
    context_object_name = "robots"


class RobotDetailView(DetailView):
    model = Robot
    template_name = "robots/detail.html"
    context_object_name = "robot"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class RobotCreateView(LoginRequiredMixin, CreateView):
    model = Robot
    template_name = "robots/form.html"
    fields = [
        "title",
        "description",
        "cover_image",
        "external_link",
    ]
    success_url = reverse_lazy("robots:list")


class RobotUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Robot
    template_name = "robots/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("robots:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class RobotDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Robot
    template_name = "robots/confirm_delete.html"
    success_url = reverse_lazy("robots:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
