from django.shortcuts import render
from projects.models import Project


def index(request):
    context = {
        "projects": Project.objects.filter(category="R"),
    }
    return render(request, "responsible_computing/index.html", context=context)
