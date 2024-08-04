from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Publication


class PublicationListView(ListView):
    model = Publication
    template_name = "publications/list.html"
    context_object_name = "publications"


class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publications/detail.html"
    context_object_name = "publicatioon"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = "publications/form.html"
    fields = [
        "title",
        "description",
        "cover_image",
        "external_link",
    ]
    success_url = reverse_lazy("publications:list")


class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    template_name = "publications/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("publications:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publication
    template_name = "publications/confirm_delete.html"
    success_url = reverse_lazy("publications:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
