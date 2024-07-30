from django.shortcuts import render


def index(request):
    return render(request, "responsible_computing/index.html")
