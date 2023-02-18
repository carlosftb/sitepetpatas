from django.shortcuts import render
from petpatas.models import Servicos




def index(request):
    servicos = Servicos.objects.order_by("nome").filter(ativo=True)
    return render(request, 'petpatas/index.html', {"cards": servicos})
def service(request):
    return render(request, "petpatas/services.html")

def about(request):
    return render(request, "petpatas/about.html")

def findus(request):
    return render(request, "petpatas/findus.py")

def login(request):
    return render(request, "petpatas/login.html")


