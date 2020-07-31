from django.shortcuts import render,redirect
from .models import Usuario
from .models import Noticia
from create.models import coordinadores,Integrante,Participante2,Rol
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

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
        user = authenticate(username=username, password=password)
        if user is not None:
            do_login(request, user)
            if(request.user.groups.filter(name='Coordinador').exists()):
                coordinador=coordinadores.objects.get(user=request.user)
                integrante=Integrante.objects.get(id=coordinador.Integrante.id)
                rol=Rol.objects.get(name="Coordinador de semillero")
                participante=Participante2.objects.filter(id_integrante=integrante.id,rol=rol)
                if(participante.count()>1):
                    return redirect('/choose')
                else:
                    return redirect('/')
            else:
                return redirect('/')        
    return render(request, "core/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        grupo = request.POST['group']
        if " " in username:
            return render(request, "core/sign-up.html", {'mensaje':'El nombre de usuario no puede contener espacios.'})
        elif rpassword == password:
            user = User.objects.create_user(username, email, password)
            group = Group.objects.all().filter(name=grupo)
            user.first_name = name
            user.last_name = lastname
            user.groups.set(group)
            user.save()
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

def choose(request):
    coordinador=coordinadores.objects.get(user=request.user)
    integrante=Integrante.objects.get(id=coordinador.Integrante.id)
    rol=Rol.objects.get(name="Coordinador de semillero")
    semilleros=Participante2.objects.filter(id_integrante=integrante.id,rol=rol)
    if request.method=="POST":
        semillero=request.POST["id_semillero"]
        insert=coordinadores.objects.get(user=request.user)
        insert.id_semillero=semillero
        insert.save(update_fields=['id_semillero'])
        return redirect("/")

    return render(request,"core/choose.html",{'semilleros':semilleros})