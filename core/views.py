from django.shortcuts import render


def home(request):
    return render(request, "core/index.html")


def admin(request):
    return render(request, "core/moderator.html")
