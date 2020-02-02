from django.shortcuts import render
from .models import Usuario
from .models import Noticia
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    noticias = Noticia.objects.all().order_by('-created')
    layers = Noticia.objects.all().order_by('-created')[:4]

    """ if request.method == "POST":
        title = request.POST['title']
        image = request.POST['image']
        description = request.POST['description']
        content = request.POST['content']

        insert = Noticia(title=title, image=image, description=description, content=content)
        insert.save()
    """

    return render(request, "core/home.html", {'noticias':noticias,'layers':layers})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, "core/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        if " " in username:
            return render(request, "core/sign-up.html", {'mensaje':'El nombre de usuario no puede contener espacios.'})
        elif rpassword == password:
            insert = Usuario(username=username, password=make_password(password), name=name, lastname=lastname, email=email)
            insert.save()
            return render(request, "core/sign-up.html")
        else:
            return render(request, "core/sign-up.html", {'mensaje':'Las contraseñas no coinciden.'})
    return render(request, "core/sign-up.html")

def add_news(request):
    if request.method == "POST":
        image = request.FILES['image']
        banner = request.FILES['banner']
        title = request.POST['title']
        description = request.POST['description']
        content = request.POST['content']
        insert = Noticia(title=title, description=description, content=content, image=image, banner=banner)
        insert.save()

    return render(request, "core/add_news.html")

def news(request, id_item=None):
    item = Noticia.objects.get(id=id_item)
    return render(request, "core/news.html",{'item':item,})