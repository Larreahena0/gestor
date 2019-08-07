from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def create(request):
    return render(request, "core/create.html")

def register(request):
    return render(request, "core/register.html")

def add_workline(request):
    return render(request, "core/add_workline.html")

def conv_create(request):
    return render(request, "core/conv_create.html")

def participate(request):
    return render(request, "core/participate.html")