from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = {}
        context["msc_projects"] = Project.objects.filter(category=Project.Msc)
        context["responsible_computing_projects"] = Project.objects.filter(
            category=Project.RE
        )
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/form.html"
    fields = [
        "title",
        "description",
        "cover_image",
        "external_link",
    ]
    success_url = reverse_lazy("projects:list")


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "projects/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("projects:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "projects/confirm_delete.html"
    success_url = reverse_lazy("projects:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
