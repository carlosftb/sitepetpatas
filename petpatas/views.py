from django.shortcuts import render


def index(request):
    return render(request, "petpatas/index.html")

def service(request):
    return render(request, "petpatas/services.html")

def about(request):
    return render(request, "petpatas/about.html")

def findus(request):
    return render(request, "petpatas/findus.py")