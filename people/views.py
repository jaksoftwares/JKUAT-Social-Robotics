from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Person


class PersonListView(ListView):
    model = Person
    template_name = "people/list.html"
    context_object_name = "people"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["postgraduates"] = Person.objects.filter(category=Person.POSTGRADUATE)
        context["undergraduates"] = Person.objects.filter(
            category=Person.UNDERGRADRUATE
        )
        context["principal_investigator"] = Person.objects.get(category=Person.PI)
        context["admin"] = Person.objects.get(category=Person.ADMIN)
        return context


class PersonDetailView(DetailView):
    model = Person
    template_name = "people/detail.html"
    context_object_name = "person"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    template_name = "people/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("people:list")


class PersonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Person
    template_name = "people/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("people:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class PersonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Person
    template_name = "people/confirm_delete.html"
    success_url = reverse_lazy("people:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
