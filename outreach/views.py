from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Outreach


class OutreachListView(ListView):
    model = Outreach
    template_name = "outreach/list.html"
    context_object_name = "outreach"


class OutreachDetailView(DetailView):
    model = Outreach
    template_name = "outreach/detail.html"
    context_object_name = "outreach"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class OutreachCreateView(LoginRequiredMixin, CreateView):
    model = Outreach
    template_name = "outreach/form.html"
    fields = [
        "title",
        "description",
        "profile_pictcover_imageure",
        "external_link",
    ]
    success_url = reverse_lazy("outreach:list")


class OutreachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Outreach
    template_name = "outreach/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("outreach:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class OutreachDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Outreach
    template_name = "outreach/confirm_delete.html"
    success_url = reverse_lazy("outreach:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
