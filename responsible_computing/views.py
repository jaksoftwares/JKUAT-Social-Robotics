from django.shortcuts import render
from projects.models import Project

def index(request):
    context = {
        "projects": Project.objects.filter(category="R"),  # Selected projects (Responsible Computing)
        "mainprojects": Project.objects.filter(category="P"),  # Featured Highlights
    }
    return render(request, "responsible_computing/index.html", context)
