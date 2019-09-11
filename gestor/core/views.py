from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def login(request):
    return render(request, "core/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        if rpassword == password:
            insert = Usuario(username=username, password=make_password(password), name=name, lastname=lastname, email=email)
            insert.save()
            return render(request, "core/sign-up.html")
        else:
            return render(request, "core/sign-up.html", {'mensaje':'Las contraseñas no coinciden.'})
    return render(request, "core/sign-up.html")
