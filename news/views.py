from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import News


class NewsListView(ListView):
    model = News
    template_name = "news/list.html"
    context_object_name = "news"


class NewsDetailView(DetailView):
    model = News
    template_name = "news/detail.html"
    context_object_name = "news"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = "news/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("news:list")


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = "news/form.html"
    fields = ["first_name", "last_name", "profile_picture", "bio"]
    success_url = reverse_lazy("news:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = "news/confirm_delete.html"
    success_url = reverse_lazy("news:list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def test_func(self):
        return self.request.user.is_staff
