from django.shortcuts import render, redirect
from .models import Semillero
from .models import Linea
from .models import LineaSemillero
from .models import Integrante
from .models import Career,Rol,Atributos
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
            pregrados = Career.objects.filter(tipo="Pregrado")
            postgrados = Career.objects.filter(tipo="Postgrado")
            lineas = Linea.objects.all()
            roles = Rol.objects.all()

            if request.method == "POST":
                name = request.POST['name']
                document = request.POST['document']
                semillero = request.POST['semillero']
                rol1 = request.POST['rol']
                joined = request.POST['joined']
                email = request.POST['email']
                phone = request.POST['phone']
                aditional = request.POST['adicional']
                #career = request.POST['career']
                #level = request.POST['level']
                rol=Rol.objects.get(id=rol1)
                insert = Integrante(name=name, document=document, semillero=semillero,
                                    rol=rol, joined=joined, email=email, phone=phone, aditional=aditional)
                insert.save()

                #Cuando es un coordinador de linea se agregan las lineas asociadas
                if(int(rol1) == 3):
                    count = int(request.POST['contador'])
                    print(count)

                    for i in range(0, count+1):
                        id_coo = Integrante.objects.latest('id')
                        id_linea = request.POST['idline_' + str(i)]
                        linea = Linea.objects.get(id=id_linea)

                        insert = LineaSemillero(
                            id_coo=id_coo, id_linea=linea)
                        insert.save()

                #Cuando es estudiante se deben agregar los atributos de los estudiantes (nivel y carrera)        
                elif(int(rol1) == 4 or int(rol1) == 5):
                    tipo = request.POST['tipo']
                    if(int(tipo) == 1):
                        id_prog = request.POST['pregrado']
                    elif(int(tipo) == 2):
                        id_prog = request.POST['postgrado']
                    programa = Career.objects.get(id=id_prog)
                    id_est = Integrante.objects.latest('id')
                    nivel = request.POST['level']
                    insert = Atributos(id_estudiante=id_est,id_programa=programa,nivel=nivel)
                    insert.save()

            return render(request, "create/register.html", {'semilleros': semilleros, 'pregrados': pregrados, 'postgrados': postgrados, 'lineas': lineas,'roles':roles})

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
