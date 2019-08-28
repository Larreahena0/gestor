from django.shortcuts import render
from .models import Semillero
from .models import Linea
from .models import Integrante
from .models import Career
from core.models import Grupo

# Create your views here.
def create(request):

    grupos = Grupo.objects.all()
    lineas = Linea.objects.all()

    if request.method == "POST":
        id_group = request.POST['id_group']
        name = request.POST['name']
        lines = request.POST['lines']
        insert = Semillero(id_group=id_group, name=name, lines=lines)
        insert.save()

    return render(request, "create/create.html", {'grupos':grupos,'lineas':lineas,})

def register(request):

    semilleros = Semillero.objects.all()
    careers = Career.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        document = request.POST['document']
        semillero = request.POST['semillero']
        rol = request.POST['rol']
        joined = request.POST['joined']
        email = request.POST['email']
        career = request.POST['career']
        level = request.POST['level']
        insert = Integrante(name=name, document=document, semillero=semillero, rol=rol, joined=joined, email=email, career=career, level=level)
        insert.save()

    return render(request, "create/register.html",{'semilleros':semilleros, 'careers': careers})

def add_workline(request):

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        insert = Linea(name=name, description=description)
        insert.save()

    return render(request, "create/workline.html")