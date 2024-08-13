from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "events/list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "events/detail.html"
    context_object_name = "event"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "events/form.html"
    fields = [
        "title",
        "description",
        "cover_image",
        "date_starting",
        "date_ending",
        "external_link",
    ]
    success_url = reverse_lazy("events:list")


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    template_name = "events/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("events:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "events/confirm_delete.html"
    success_url = reverse_lazy("events:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
