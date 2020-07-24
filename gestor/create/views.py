from django.shortcuts import render, redirect,HttpResponse
from .models import Semillero
from .models import Linea
from .models import LineaSemillero
from .models import Integrante
from .models import Career,Rol,Atributos,coordinadores,Participante2
from core.models import Grupo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.


def create(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            grupos = Grupo.objects.all()
            lineas = Linea.objects.all()
            semilleros = Semillero.objects.all()

            if request.method == "POST":
                if request.POST['caso'] == "verificar":
                    cedula = request.POST['cc']
                    try:
                        integrante = Integrante.objects.get(document=cedula)
                        try:
                            coordinador = coordinadores.objects.get(Integrante=integrante)
                            #Se debe asignar el coordinador y integrante existente al semillero
                            return HttpResponse("1")
                        except:
                            #Se debe crear el perfil coordinador y se debe asignar el integrante existente al semillero
                            return HttpResponse("2")
                    except:    
                        #Se debe crear el coordinador y integrante al semillero
                        return HttpResponse("3")
                elif request.POST['caso']=="2" or request.POST['caso']=="3":
                    username = request.POST['user']
                    password = request.POST['password']
                    rpassword = request.POST['rpassword']  
                    grupo = request.POST['group']
                    cc = request.POST['cc']
                    if " " in username:
                        return HttpResponse("1")    
                    elif rpassword == password:
                        try:
                            user=User.objects.get(username=username)
                            return HttpResponse("4")
                        except:
                            user = User.objects.create_user(username,"", password)
                            group = Group.objects.all().filter(name=grupo)
                            user=User.objects.get(username=username)
                            user.groups.set(group)
                            user.save()
                            if request.POST['caso']=="3":
                                name = request.POST['name']
                                lastname = request.POST['lastname']
                                email = request.POST['email']
                                phone = request.POST['phone']
                                adicional = request.POST['adicional']
                                insert = Integrante(name=name,lastname=lastname,document=cc,email=email,phone=phone,aditional=adicional)
                                insert.save()
                            integrante = Integrante.objects.get(document=cc)
                            user.first_name = integrante.name
                            user.last_name = integrante.lastname
                            user.email = integrante.email
                            user.save()
                            insert = coordinadores(Integrante=integrante,user=user)
                            insert.save()
                            return HttpResponse("2")
                    else:
                        return HttpResponse("3")
                #Funcion donde se crea el semillero       
                elif request.POST['caso']=="1":
                    '''
                    if 'lista' in request.POST:

                        id = request.POST['lista']

                        instance = Semillero.objects.get(id=id)
                        instance.delete()

                    elif 'id_group' in request.POST:'''
                    group = request.POST['id_group']
                    id_group=Grupo.objects.get(id=group)
                    name = request.POST['name']
                    history = request.POST['history']
                    mision = request.POST['mision']
                    vision = request.POST['vision']
                    goals = request.POST['goals']
                    document=request.POST['cc']
                    integrante=Integrante.objects.get(document=document)

                    insert = Semillero(
                        id_group=id_group, name=name, history=history, mision=mision, vision=vision, goals=goals,coordinador=integrante)
                    insert.save()

                    joined=request.POST['joined']
                    semillero=Semillero.objects.latest('id')
                    rol=Rol.objects.get(name="Coordinador de semillero")
                    insert=Participante2(id_integrante=integrante,id_semillero=semillero,rol=rol,joined=joined)
                    insert.save()
                    return HttpResponse("1")

                elif request.POST['caso']=="eliminar":
                    id_s=request.POST['id']
                    semillero=Semillero.objects.get(id=id_s)
                    semillero.delete()
            return render(request, "create/create.html", {'grupos': grupos, 'lineas': lineas, 'Semilleros': semilleros})

    return redirect('/')


def semillero_edit(request, id):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            semilleros = Semillero.objects.all()
            semillero = Semillero.objects.get(id=id)
            grupos = Grupo.objects.all()

            if request.method == "POST":

                group = request.POST['id_group']
                id_group=Grupo.objects.get(id=group)
                name = request.POST['name']
                history = request.POST['history']
                mision = request.POST['mision']
                vision = request.POST['vision']
                goals = request.POST['goals']

                insert = Semillero.objects.get(id=id)
                insert.id_group=id_group
                insert.name=name
                insert.history=history
                insert.mision=mision
                insert.vision=vision
                insert.goals=goals
                insert.save(update_fields=['id_group','name','history','mision','vision','goals'])

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

def semillero_details(request,id):
    if request.user.is_authenticated:
        semillero=Semillero.objects.get(id=id)
        integrantes = Participante2.objects.filter(id_semillero=semillero)
        return render(request, "create/details.html",{"semillero":semillero,"integrantes":integrantes})

    return redirect('/')
def produccion(request):

    return render(request, "create/produccion.html")
