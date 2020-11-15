from django.shortcuts import render, redirect,HttpResponse
from .models import Semillero
from .models import Linea
from .models import LineaSemillero
from .models import Integrante
from .models import Career,Rol,Atributos,coordinadores,Participante2,Atributos_otra,categoriaAdyacente,categoriaPrincipal,produccion
from core.models import Grupo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from functools import reduce
from operator import or_
from django.db.models import Q


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
                            return HttpResponse("1,"+integrante.name+" "+integrante.lastname)
                        except:
                            #Se debe crear el perfil coordinador y se debe asignar el integrante existente al semillero
                            return HttpResponse("2,"+integrante.name+" "+integrante.lastname)
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
                            return HttpResponse("2,"+integrante.name+" "+integrante.lastname)
                    else:
                        return HttpResponse("3")
                #Funcion donde se crea el semillero       
                elif request.POST['caso']=="1":
                    group = request.POST['id_group']
                    id_group=Grupo.objects.get(id=group)
                    name = request.POST['name_s']
                    mail = request.POST['mail']
                    description = request.POST['description']
                    document=request.POST['coordinador']
                    integrante=Integrante.objects.get(document=document)

                    try:
                        image = request.FILES['image']
                        insert = Semillero(id_group=id_group, name=name, description=description,coordinador=integrante,mail=mail,image=image)
                        insert.save()
                    except:
                        insert = Semillero(id_group=id_group, name=name, description=description,coordinador=integrante,mail=mail)
                        insert.save()

                    joined=request.POST['joined']
                    semillero=Semillero.objects.latest('id')
                    rol=Rol.objects.get(name="Coordinador de semillero")
                    insert=Participante2(id_integrante=integrante,id_semillero=semillero,rol=rol,joined=joined)
                    insert.save()

                    coordinador = coordinadores.objects.get(Integrante=integrante)
                    coordinador.id_semillero = semillero.id
                    coordinador.save(update_fields=["id_semillero"])

                elif request.POST['caso']=="eliminar":
                    id_s=request.POST['id']
                    semillero=Semillero.objects.get(id=id_s)
                    #Se debe verificar si el coordinador es coordinador de mas de un semillero
                    rol = Rol.objects.get(name="Coordinador de semillero")
                    integrante = Integrante.objects.get(id=int(semillero.coordinador.id))
                    semillero.delete()
                    semilleros = Participante2.objects.filter(id_integrante=integrante,rol=rol)
                    #Si era unico coordinador no tiene sentido que siga teniendo usuario en la app
                    if(semilleros.count()==0):
                        old_c = coordinadores.objects.get(Integrante=integrante)
                        user = User.objects.get(id=old_c.user.id)
                        old_c.delete()
                        user.delete()
                    #En caso de ser coordiandor se modifica el campo id_semilero por si fue el ultimo seleccionado por el coordinador                   
                    else:
                        coordinador = coordinadores.objects.get(Integrante=integrante)
                        for semillero in semilleros:
                            coordinador.id_semillero = semillero.id_semillero.id
                            coordinador.save(update_fields=["id_semillero"])

            return render(request, "create/create.html", {'grupos': grupos, 'lineas': lineas, 'Semilleros': semilleros})

    return redirect('/')


def semillero_edit(request, id):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            semilleros = Semillero.objects.all()
            semillero = Semillero.objects.get(id=id)
            grupos = Grupo.objects.all()

            if request.method == "POST":
                if request.POST['caso'] == "verificar":
                    cedula = request.POST['cc']
                    try:
                        integrante = Integrante.objects.get(document=cedula)
                        try:
                            coordinador = coordinadores.objects.get(Integrante=integrante)
                            #Se debe asignar el coordinador y integrante existente al semillero
                            return HttpResponse("1,"+integrante.name+" "+integrante.lastname)
                        except:
                            #Se debe crear el perfil coordinador y se debe asignar el integrante existente al semillero
                            return HttpResponse("2,"+integrante.name+" "+integrante.lastname)
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
                            insert = coordinadores(Integrante=integrante,user=user,id_semillero=id)
                            insert.save()
                            return HttpResponse("2,"+integrante.name+" "+integrante.lastname)
                    else:
                        return HttpResponse("3")
                elif request.POST["caso"] == "1":
                    #Edicion del coordinador 
                    semillero = Semillero.objects.get(id=id)
                    new_coord = request.POST["cc"]
                    if(new_coord != semillero.coordinador.document):
                        #El coordinador cambió por tanto se debe actualizar el coordinador
                        old_coord = semillero.coordinador.document
                        rol = Rol.objects.get(name="Coordinador de semillero")
                        participante = Participante2.objects.get(id_semillero=semillero,rol=rol)
                        integrante = Integrante.objects.get(document=new_coord)
                        participante.id_integrante=integrante
                        participante.save(update_fields=["id_integrante"])
                        semillero.coordinador=integrante
                        semillero.save(update_fields=["coordinador"])
                        #Se debe verificar si el coordinador es coordinador de mas de un semillero
                        integrante = Integrante.objects.get(document=old_coord)
                        semilleros = Participante2.objects.filter(id_integrante=integrante,rol=rol)
                        #Si era unico coordinador no tiene sentido que siga teniendo usuario en la app
                        if(semilleros.count()==0):
                            old_c = coordinadores.objects.get(Integrante=integrante)
                            user = User.objects.get(id=old_c.user.id)
                            old_c.delete()
                            user.delete()
                        else:
                            print("no eliminar coordinador")

                    #Edicion de los campos principales del semillero
                    group = request.POST['id_group']
                    id_group=Grupo.objects.get(id=group)
                    name = request.POST['name']
                    description = request.POST['description']
                    mail = request.POST['mail']
                    insert = Semillero.objects.get(id=id)
                    insert.id_group=id_group
                    insert.name=name
                    insert.description=description
                    insert.mail=mail
                    insert.save(update_fields=['id_group','name','description','mail'])

                    return HttpResponse("2")

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
            
            id_semillero=int(coordinadores.objects.get(user=request.user).id_semillero)
            semillero = Semillero.objects.get(id=id_semillero)
            integrantes = Participante2.objects.filter(id_semillero=semillero)
            pregrados = Career.objects.filter(tipo="Pregrado")
            postgrados = Career.objects.filter(tipo="Postgrado")
            lineas = Linea.objects.all()
            #query = reduce(or_, (Q(name="Coordinador de grupo"),Q(name="Coordinador de linea"),Q(name="Estudiante lider"),Q(name="Estudiante Udea"),Q(name="Estudiante de otra institucion")))
            #roles = Rol.objects.filter(query)
            roles = Rol.objects.all().exclude(id=2)

            if request.method == "POST":
                if request.POST['caso']=="verificar":
                    cedula = request.POST['cc']
                    try:
                        #Si existe perfil integrante se retorna 1
                        integrante = Integrante.objects.get(document=cedula)
                        try:
                            id_semillero=int(coordinadores.objects.get(user=request.user).id_semillero)
                            semillero = Semillero.objects.get(id=id_semillero)
                            participante = Participante2.objects.get(id_integrante=integrante,id_semillero=semillero)
                            return HttpResponse("3,"+integrante.name+" "+integrante.lastname)
                        except:    
                            return HttpResponse("1,"+integrante.name+" "+integrante.lastname)
                    except:    
                        #Si no existe perfil integrante se retorna 2
                        return HttpResponse("2")
                
                elif request.POST["caso"]=="eliminar":
                    id = request.POST["id"]
                    insert = Participante2.objects.get(id=id)
                    insert.delete()

                elif request.POST['caso']=="nuevo" or request.POST['caso']=="viejo":
                    if request.POST['caso']=="nuevo":        
                        name = request.POST['name']
                        lastname = request.POST['lastname']
                        document = request.POST['document']
                        email = request.POST['email']
                        phone = request.POST['phone']
                        aditional = request.POST['adicional']
                        insert = Integrante(name=name,lastname=lastname, document=document, email=email, phone=phone, aditional=aditional)
                        insert.save()

                    semillero = request.POST['semillero']
                    document = request.POST['document']
                    rol1 = request.POST['rol']
                    joined = request.POST['joined']
                    rol=Rol.objects.get(id=rol1)
                    semillero=Semillero.objects.get(id=semillero)
                    integrante = Integrante.objects.get(document=document)
                    insert = Participante2(id_integrante=integrante,id_semillero=semillero,rol=rol,joined=joined)
                    insert.save()

                    #Cuando es un coordinador de linea se agregan las lineas asociadas
                    if(int(rol1) == 3):
                        count = int(request.POST['contador'])
                        print(count)

                        for i in range(0, count+1):
                            id_coo = Integrante.objects.get(document=document)
                            id_linea = request.POST['idline_' + str(i)]
                            linea = Linea.objects.get(id=id_linea)
                            participante=Participante2.objects.latest('id')
                            insert = LineaSemillero(
                                id_coo=id_coo, id_linea=linea, id_participante=participante)
                            insert.save()

                    #Cuando es estudiante UDEA se deben agregar los atributos de los estudiantes (nivel y carrera)        
                    elif(int(rol1) == 4 or int(rol1) == 5):
                        tipo = request.POST['tipo']
                        if(int(tipo) == 1):
                            id_prog = request.POST['pregrado']
                        elif(int(tipo) == 2):
                            id_prog = request.POST['postgrado']
                        programa = Career.objects.get(id=id_prog)
                        id_est = Integrante.objects.get(document=document)
                        nivel = request.POST['level']
                        participante=Participante2.objects.latest('id')
                        insert = Atributos(id_estudiante=id_est,id_programa=programa,id_participante=participante,nivel=nivel)
                        insert.save()

                    #Cuando es estudiante de otra universidad      
                    elif(int(rol1) == 7):
                        tipo = request.POST['tipo_otra']
                        participante=Participante2.objects.latest('id')
                        id_est = Integrante.objects.get(document=document)
                        insert = Atributos_otra(id_estudiante=id_est,id_participante=participante,tipo=tipo)
                        insert.save()

            return render(request, "create/register.html", {'semillero': semillero, 'pregrados': pregrados, 'postgrados': postgrados, 'lineas': lineas,'roles':roles,'integrantes':integrantes})

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
    semillero=Semillero.objects.get(id=id)
    integrantes = Participante2.objects.filter(id_semillero=semillero)
    return render(request, "create/details.html",{"semillero":semillero,"integrantes":integrantes})

def integrante_details(request,id):
    if request.user.is_authenticated:
        integrante = Integrante.objects.get(id=id)
        coordinador = coordinadores.objects.get(user=request.user)
        semillero = Semillero.objects.get(id=int(coordinador.id_semillero))
        participante = Participante2.objects.get(id_integrante=integrante,id_semillero=semillero)
        if(participante.rol.name=="Coordinador de linea"):
            linea_coordinador = LineaSemillero.objects.filter(id_coo=integrante,id_participante=participante)
            return render(request, "create/integrante.html",{"integrante":integrante,"participante":participante,"linea_coordinador":linea_coordinador})

        elif(participante.rol.name=="Estudiante Udea" or participante.rol.name=="Estudiante lider"):
            atributo = Atributos.objects.get(id_estudiante=integrante,id_participante=participante)
            return render(request, "create/integrante.html",{"integrante":integrante,"participante":participante,"atributo":atributo})

        elif(participante.rol.name=="Estudiante de otra institucion"):
            atributo = Atributos_otra.objects.get(id_estudiante=integrante,id_participante=participante)
            return render(request, "create/integrante.html",{"integrante":integrante,"participante":participante,"atributo_otra":atributo})

        else:    
            return render(request, "create/integrante.html",{"integrante":integrante,"participante":participante})
    return redirect('/')

def integrante_edit(request, id):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Coordinador").exists():

            integrante = Integrante.objects.get(id=id)
            coordinador = coordinadores.objects.get(user=request.user)
            participante = Participante2.objects.get(id_integrante=integrante,id_semillero=int(coordinador.id_semillero))
            #query = reduce(or_, (Q(name="Coordinador de grupo"),Q(name="Coordinador de linea"),Q(name="Estudiante lider"),Q(name="Estudiante Udea"),Q(name="Estudiante de otra institucion")))
            #roles = Rol.objects.filter(query)
            roles = Rol.objects.all().exclude(id=2)
            lineas = Linea.objects.all()
            pregrados = Career.objects.filter(tipo="Pregrado")
            postgrados = Career.objects.filter(tipo="Postgrado")

            if request.method == "POST":

                #Edicion de datos principales
                name = request.POST["name"]
                lastname = request.POST["lastname"]
                document = request.POST["document"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                aditional = request.POST["adicional"]
                integrante=Integrante.objects.get(id=id)
                integrante.name = name
                integrante.lastname = lastname
                integrante.document = document
                integrante.email = email
                integrante.phone = phone
                integrante.aditional = aditional
                integrante.save(update_fields=["name","lastname","document","phone","email","aditional"])
                
                #Edicion del rol en el semillero
                integrante=Integrante.objects.get(id=id)
                coordinador = coordinadores.objects.get(user=request.user)
                participante = Participante2.objects.get(id_integrante=integrante,id_semillero=int(coordinador.id_semillero))
                rol = request.POST["rol"]
                if int(rol) != participante.rol.id:
                    #Cambio de rol, se debe eliminar atributos en caso de ser estudiante y eliminar lineas en caso de ser coordinador de linea
                    if(participante.rol.name == "Estudiante Udea" or participante.rol.name == "Estudiante lider"):
                        atributo = Atributos.objects.get(id_participante=participante)
                        atributo.delete()

                    elif(participante.rol.name == "Coordinador de linea"):
                        lineas = LineaSemillero.objects.filter(id_participante=participante)
                        for linea in lineas:
                            linea.delete()

                    elif(participante.rol.name == "Estudiante de otra institucion"):
                        atributo = Atributos_otra.objects.get(id_participante=participante)
                        atributo.delete()

                    #Actualizacion del rol y de la fecha de ingreso al semillero
                    rol1 = Rol.objects.get(id=int(rol))
                    participante.rol=rol1
                    participante.joined=request.POST["joined"]
                    participante.save(update_fields=["rol","joined"])

                    #Creacion de los atributos en caso de ser estudiante o ser coordinador de linea
                    participante = Participante2.objects.get(id_integrante=integrante,id_semillero=int(coordinador.id_semillero))
                    #Cuando es un coordinador de linea se agregan las lineas asociadas
                    if(int(rol) == 3):
                        count = int(request.POST['contador'])
                        print(count)

                        for i in range(0, count+1):
                            id_coo = Integrante.objects.get(document=document)
                            id_linea = request.POST['idline_' + str(i)]
                            linea = Linea.objects.get(id=id_linea)

                            insert = LineaSemillero(
                                id_coo=id_coo, id_linea=linea, id_participante=participante)
                            insert.save()

                    #Cuando es estudiante se deben agregar los atributos de los estudiantes (nivel y carrera)        
                    elif(int(rol) == 4 or int(rol) == 5):
                        tipo = request.POST['tipo']
                        if(int(tipo) == 1):
                            id_prog = request.POST['pregrado']
                        elif(int(tipo) == 2):
                            id_prog = request.POST['postgrado']
                        programa = Career.objects.get(id=id_prog)
                        id_est = Integrante.objects.get(document=document)
                        nivel = request.POST['level']
                        insert = Atributos(id_estudiante=id_est,id_programa=programa,id_participante=participante,nivel=nivel)
                        insert.save()

                    #Cuando es estudiante de otra universidad se agrega el tipo de estudiante unicamente
                    elif(int(rol) == 7):
                        tipo = request.POST['tipo_otra']
                        id_est = Integrante.objects.get(document=document)
                        insert = Atributos_otra(id_estudiante=id_est,id_participante=participante,tipo=tipo)
                        insert.save()    

                else:
                    integrante=Integrante.objects.get(id=id)
                    coordinador = coordinadores.objects.get(user=request.user)
                    participante = Participante2.objects.get(id_integrante=integrante,id_semillero=int(coordinador.id_semillero))
                    
                    #En caso de ser un estudiante, se debe actualizar la carrera y nivel del integrante
                    if(participante.rol.name == "Estudiante Udea" or participante.rol.name == "Estudiante lider"):
                        atributo = Atributos.objects.get(id_participante=participante)
                        tipo = request.POST['tipo']
                        if(int(tipo) == 1):
                            id_prog = request.POST['pregrado']
                        elif(int(tipo) == 2):
                            id_prog = request.POST['postgrado']
                        programa = Career.objects.get(id=id_prog)
                        atributo.id_programa = programa
                        atributo.nivel = request.POST["level"]
                        atributo.save(update_fields=["id_programa","nivel"])
                    
                    #En caso de ser estudiante de otra institucion se debe actualizar el tipo de estudiante
                    elif(participante.rol.name == "Estudiante de otra institucion"):
                        atributo = Atributos_otra.objects.get(id_participante=participante)
                        tipo = request.POST['tipo_otra']
                        atributo.tipo = tipo
                        atributo.save(update_fields=["tipo"])

                    #En caso de ser un coordinador de linea se deben eliminar las ultimas n lineas o se deben agregar n lineas.
                    elif(participante.rol.name == "Coordinador de linea"):
                        contador=request.POST["contador"]

                        if int(contador)<-1:
                            count = int(request.POST['contador'])+1
                            linea_coordinador = LineaSemillero.objects.filter(id_coo=integrante,id_participante=participante)
                            count = count + linea_coordinador.count()
                            var = 0
                            for linea in linea_coordinador:
                                if(var>=count):
                                    linea.delete()
                                else:
                                    var+=1    

                        elif int(contador)>-1:
                            count = int(request.POST['contador'])
                            for i in range(0, count+1):
                                id_coo = Integrante.objects.get(document=document)
                                id_linea = request.POST['idline_' + str(i)]
                                linea = Linea.objects.get(id=id_linea)

                                insert = LineaSemillero(
                                    id_coo=id_coo, id_linea=linea, id_participante=participante)
                                insert.save()

                    #Finalmente se actualiza la fecha de ingreso al semillero
                    participante.joined=request.POST["joined"]
                    participante.save(update_fields=["joined"])        
                
                return redirect("register")

            if(participante.rol.name=="Coordinador de linea"):
                linea_coordinador = LineaSemillero.objects.filter(id_coo=integrante,id_participante=participante)
                return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"lineas":lineas,"integrante":integrante,"participante":participante,'roles':roles,"linea_coordinador":linea_coordinador})

            elif(participante.rol.name=="Estudiante Udea" or participante.rol.name=="Estudiante lider"):
                atributo = Atributos.objects.get(id_estudiante=integrante,id_participante=participante)
                if(atributo.id_programa.tipo=="Pregrado"):
                    return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"pregrado":"pregrado","lineas":lineas,"integrante":integrante,"participante":participante,'roles':roles,"atributo":atributo})
                else:
                    return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"postgrado":"postgrado","lineas":lineas,"integrante":integrante,"participante":participante,'roles':roles,"atributo":atributo})
            elif(participante.rol.name=="Estudiante de otra institucion"):
                atributo = Atributos_otra.objects.get(id_estudiante=integrante,id_participante=participante)
                if(atributo.tipo == "1"):
                    return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"tipo":"pregrado","lineas":lineas,"integrante":integrante,"participante":participante,'roles':roles,"atributo":atributo})
                else:
                    return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"tipo":"postgrado","lineas":lineas,"integrante":integrante,"participante":participante,'roles':roles,"atributo":atributo})
            else:    
                return render(request, "create/integrante_edit.html",{'pregrados': pregrados, 'postgrados': postgrados,"lineas":lineas,'integrante': integrante, 'participante': participante,'roles':roles})

def editar(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Coordinador").exists():
            id_semillero = coordinadores.objects.get(user=request.user).id_semillero
            semillero = Semillero.objects.get(id=int(id_semillero))
            if request.method == "POST":
                mail = request.POST["mail"]
                history = request.POST['history']
                mision = request.POST['mision']
                vision = request.POST['vision']
                goals = request.POST['goals']
                description = request.POST["description"]
                try:
                    image = request.FILES["image"]
                except:
                    image = ""

                semillero.history=history
                semillero.mision=mision
                semillero.goals=goals
                semillero.vision=vision
                semillero.mail = mail
                semillero.description = description
                if(image!=""):
                    semillero.image = image
                    semillero.save(update_fields=["history","vision","goals","mision","mail","description","image"])
                else:
                    semillero.save(update_fields=["history","vision","goals","mision","mail","description"])
        else:
            return redirect("create")
    else:
        return redirect("/")

    return render(request, "create/edit.html",{'semillero':semillero})


def produccion(request):
    
    principales = categoriaPrincipal.objects.all()
    generacionConocimiento = categoriaPrincipal.objects.get(nombre='Generación de nuevo conocimiento')
    produccionTecnica = categoriaPrincipal.objects.get(nombre='Producción técnica y tecnológica')
    productoDivulgacion = categoriaPrincipal.objects.get(nombre='Productos de divulgación')
    adyacenteGeneracion = categoriaAdyacente.objects.filter(categoria=generacionConocimiento)
    adyacenteProduccion = categoriaAdyacente.objects.filter(categoria=produccionTecnica)
    adyacenteProducto = categoriaAdyacente.objects.filter(categoria=productoDivulgacion)

    return render(request, "create/produccion.html",{'principales':principales,'Generaciones':adyacenteGeneracion,'Producciones':adyacenteProduccion,'Productos':adyacenteProducto})