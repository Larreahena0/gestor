from django.shortcuts import render, redirect
from .models import Semillero
from .models import Linea
from .models import LineaSemillero
from .models import Integrante
from .models import Career
from core.models import Grupo

# Create your views here.


def create(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            grupos = Grupo.objects.all()
            lineas = Linea.objects.all()
            semilleros = Semillero.objects.all()

            if request.method == "POST":

                if 'lista' in request.POST:

                    id = request.POST['lista']

                    instance = Semillero.objects.get(id=id)
                    instance.delete()

                elif 'id_group' in request.POST:

                    id_group = request.POST['id_group']
                    name = request.POST['name']
                    history = request.POST['history']
                    mision = request.POST['mision']
                    vision = request.POST['vision']
                    goals = request.POST['goals']

                    insert = Semillero(
                        id_group=id_group, name=name, history=history, mision=mision, vision=vision, goals=goals)
                    insert.save()

            return render(request, "create/create.html", {'grupos': grupos, 'lineas': lineas, 'semilleros': semilleros})

    return redirect('/')


def semillero_edit(request, id):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            semilleros = Semillero.objects.all()
            semillero = Semillero.objects.get(id=id)
            grupos = Grupo.objects.all()

            if request.method == "POST":

                id_group = request.POST['id_group']
                name = request.POST['name']
                history = request.POST['history']
                mision = request.POST['mision']
                vision = request.POST['vision']
                goals = request.POST['goals']

                insert = Semillero(id=id, id_group=id_group, name=name,
                                   history=history, mision=mision, vision=vision, goals=goals)
                insert.save()

                return redirect('create')

            return render(request, "create/create_edit.html",
                          {'grupos': grupos, 'semillero': semillero, 'semilleros': semilleros})

    return redirect('/')


def semillero_delete(request, id):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            semillero = Semillero.objects.get(id=id)
            grupos = Grupo.objects.all()

            if request.method == "POST":
                id_group = request.POST['id_group']
                name = request.POST['name']

                insert = Semillero(id=id, id_group=id_group, name=name)
                insert.save()

                return redirect('create')

            return render(request, "create/create_edit.html", {'grupos': grupos, 'semillero': semillero})

    return redirect('/')


def register(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Coordinador").exists():

            semilleros = Semillero.objects.all()
            careers = Career.objects.all()
            lineas = Linea.objects.all()

            if request.method == "POST":
                name = request.POST['name']
                document = request.POST['document']
                semillero = request.POST['semillero']
                rol = request.POST['rol']
                joined = request.POST['joined']
                email = request.POST['email']
                career = request.POST['career']
                level = request.POST['level']
                insert = Integrante(name=name, document=document, semillero=semillero,
                                    rol=rol, joined=joined, email=email, career=career, level=level)
                insert.save()

                count = int(request.POST['contador'])
                print(count)

                for i in range(0, count+1):
                    id_coo = Integrante.objects.latest('id')
                    name = request.POST['line_' + str(i)]
                    id_linea = request.POST['idline_' + str(i)]

                    insert = LineaSemillero(
                        id_coo=id_coo, name=name, id_linea=id_linea)
                    insert.save()

            return render(request, "create/register.html", {'semilleros': semilleros, 'careers': careers, 'lineas': lineas})

    return redirect('/')


def add_workline(request):

    if request.user.is_authenticated:
        if request.user.groups.filter(name="Coordinador").exists():
            if request.method == "POST":
                name = request.POST['name']
                description = request.POST['description']
                insert = Linea(name=name, description=description)
                insert.save()

            return render(request, "create/workline.html")

    return redirect('/')


def produccion(request):

    return render(request, "create/produccion.html")
