from django.shortcuts import render, redirect,HttpResponse
from .models import Convocatoria
from .models import Documento,Participante,Documento_Adjunto,Proyectos,Documentos_proyecto,Documentos_proyecto_2,observaciones
from create.models import coordinadores,Semillero
from core.models import Grupo
from django.conf import settings
from django.contrib.auth.models import User

import datetime

# Create your views here.
def conv_create(request):

    if request.user.is_authenticated:
        if request.user.groups.filter(name="Administrador").exists():
            convocatorias = Convocatoria.objects.all()

            if request.method == "POST":

                estado = int(request.POST['estado'])

                if estado == 0:
                    print("Hola")
                    name = request.POST['name']
                    description = request.POST['description']
                    opened = request.POST['opened']
                    closed = request.POST['closed']

                    insert = Convocatoria(name=name, description=description, opened=opened, closed=closed)
                    insert.save()

                    count = int(request.POST['contador'])
                    
                    for i in range(1,count+1):
                        id_conv = Convocatoria.objects.latest('id')
                        docs = request.POST
                        campos = request.FILES
                        print(docs)
                        print(campos)
                        documento = request.FILES['doc_' + str(i)]
                        tipo = request.POST['sel_' + str(i)]
                        description = request.POST['text_' + str(i)]

                        insert = Documento(id_conv=id_conv, tipo=tipo, description=description, documento=documento)
                        insert.save()

                elif estado == 1:
                    conv = Convocatoria.objects.get(id=request.POST['lista'])
                    conv.delete()

                else:
                    print("Hola")
                    conv = Convocatoria.objects.get(id=request.POST['sName'])
                    id_conv = conv.id
                    name_conv = conv.name
                    description = request.POST['description']
                    opened = request.POST['opened']
                    closed = request.POST['closed']

                    insert = Convocatoria(id=id_conv, name=name_conv, description=description, opened=opened, closed=closed)
                    insert.save()

                    count = int(request.POST['contador'])

                    for i in range(1,count+1):
                        id_conv = Convocatoria.objects.latest('id')
                        documento = request.FILES['doc_' + str(i)]
                        tipo = request.POST['sel_' + str(i)]
                        description = request.POST['text_' + str(i)]

                        insert = Documento(id_conv=id_conv, tipo=tipo, description=description, documento=documento)
                        insert.save()

            today = datetime.datetime.now().strftime("%Y-%m-%d")

            return render(request, "conv/convocatoria.html",{'today':today,'convocatorias':convocatorias})

    return redirect('/')

def conv_details(request, id_item=None):
    grupos = Grupo.objects.all()
    today = datetime.datetime.now()
    item = Convocatoria.objects.get(id=id_item)
    inf_documents = Documento.objects.filter(id_conv=id_item,tipo=1)
    opc_documents = Documento.objects.filter(id_conv=id_item,tipo=2)
    obl_documents = Documento.objects.filter(id_conv=id_item,tipo=3)
    participantes = Participante.objects.filter(id_convocatoria=id_item)

    if request.method == "POST":
        #Insert de la participacion del semilero escogido por el usuario
        id_semillero = coordinadores.objects.get(user=request.user).id_semillero
        semillero = Semillero.objects.get(id=int(id_semillero))

        try:
            participante = Participante.objects.get(id_convocatoria=item,id_semillero=semillero)
            mensaje = "El semillero ya está participando en la convocatoria."
            mensaje1 = "Error"
            return render(request, "conv/details.html",{'participantes':participantes,'grupos':grupos,'item':item,'inf_documents':inf_documents,'opc_documents':opc_documents,'obl_documents':obl_documents,'today':today,"mensaje":mensaje,"mensaje1":mensaje1})
        except:
            insert = Participante(id_convocatoria=item,id_semillero=semillero,estado="0")
            insert.save()
            #Insert de los documentos obligatorios adjuntos por el coordinador de semillero
            participante = Participante.objects.latest("id")
            for obl_document in obl_documents:
                try:
                    document = request.FILES[str(obl_document.id)]
                    insert = Documento_Adjunto(id_participante=participante,id_documento=obl_document,documento=document,estado="0")
                    insert.save()
                except:
                    print("no se adjuntó")

            for opc_document in opc_documents:
                try:
                    document = request.FILES[str(opc_document.id)]
                    insert = Documento_Adjunto(id_participante=participante,id_documento=opc_document,documento=document,estado="0")
                    insert.save()
                except:
                    print("no se adjuntó")
            mensaje = "El semillero fue registrado en la convocatoria."
            mensaje1 = "Exito"
            return render(request, "conv/details.html",{'participantes':participantes,'grupos':grupos,'item':item,'inf_documents':inf_documents,'opc_documents':opc_documents,'obl_documents':obl_documents,'today':today,"mensaje":mensaje,"mensaje1":mensaje1})

    return render(request, "conv/details.html",{'participantes':participantes,'grupos':grupos,'item':item,'inf_documents':inf_documents,'opc_documents':opc_documents,
        'obl_documents':obl_documents,'today':today,})

def participar(request):
    if request.method == "POST":
        estado = int(request.POST['estado'])
        print(estado)
        if estado == 0:
            name = request.POST['name']
            description = request.POST['description']
            opened = request.POST['opened']
            closed = request.POST['closed']
            insert = Convocatoria(name=name, description=description, opened=opened, closed=closed)
            insert.save()
            count = int(request.POST['contador'])
            for i in range(1,count+1):
                try:
                    convocatoria=Convocatoria.objects.latest('id')
                    tipo = request.POST['sel_' + str(i)]
                    description = request.POST['text_' + str(i)]
                    try:
                        documento = request.FILES['doc_' + str(i)]
                        insert = Documento(id_conv=convocatoria, tipo=tipo, description=description, documento=documento)
                        insert.save()
                    except:
                        insert = Documento(id_conv=convocatoria, tipo=tipo, description=description)
                        insert.save()
                        print("No se adjunto archivo")                  
                except:
                    print("No se puede agregar el archivo ya que fue eliminado en frontend")
                    
        elif estado == 1:
            conv = Convocatoria.objects.get(id=request.POST['conv'])
            conv.delete()

    today = datetime.datetime.now()
    convocatorias = Convocatoria.objects.all()
    if request.user.groups.filter(name="Coordinador").exists():
        id_semillero = coordinadores.objects.get(user=request.user).id_semillero
        semillero = Semillero.objects.get(id=int(id_semillero))
        participaciones = Participante.objects.filter(id_semillero=semillero)
        return render(request, "conv/participate.html",{'semillero':semillero,'convocatorias':convocatorias,'today':today,'participaciones':participaciones})    
    else:
        return render(request, "conv/participate.html",{'convocatorias':convocatorias,'today':today})

def convocatoria_edit(request, id=None):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Administrador").exists():

            convocatoria = Convocatoria.objects.get(id=id)
            documentos = Documento.objects.filter(id_conv=id)

            if request.method == "POST":
                if request.POST['caso'] == "eliminar":
                    id = request.POST['id']
                    documento = Documento.objects.get(id=id)
                    documento.delete()

                elif request.POST['caso'] == "editar":   
                    name = request.POST['name']
                    description = request.POST['description']
                    opened = request.POST['opened']
                    closed = request.POST['closed']
                    insert = Convocatoria(id=id, name=name, description=description,opened=opened, closed=closed)
                    insert.save()
                    count = int(request.POST['contador'])
                    for i in range(1,count+1):
                        try:
                            convocatoria=Convocatoria.objects.latest('id')
                            tipo = request.POST['sel_' + str(i)]
                            description = request.POST['text_' + str(i)]
                            try:
                                documento = request.FILES['doc_' + str(i)]
                                insert = Documento(id_conv=convocatoria, tipo=tipo, description=description, documento=documento)
                                insert.save()
                            except:
                                insert = Documento(id_conv=convocatoria, tipo=tipo, description=description)
                                insert.save()
                                print("No se adjunto archivo")        
                        except:
                            print("No se puede agregar el archivo ya que fue eliminado en frontend")

                return redirect('participar')

            return render(request, "conv/convocatoria_edit.html",{'convocatoria': convocatoria,'documentos':documentos})

    return redirect('/')

def adjuntos(request, id, id_conv):
    if request.user.groups.filter(name="Administrador").exists() or request.user.groups.filter(name="Coordinador").exists():
        convocatoria = Convocatoria.objects.get(id=id_conv)
        semillero = Semillero.objects.get(id=id)
        participante = Participante.objects.get(id_convocatoria=convocatoria,id_semillero=semillero)
        documentos = Documento_Adjunto.objects.filter(id_participante=participante)
        if request.method == "POST":
            print(request.POST["caso"])
            if request.POST["caso"]=="1":
                id = request.POST["id_d"]
                original = Documento_Adjunto.objects.get(id=id)
                documento = request.FILES["doc"]
                original.estado=0
                original.documento=documento
                original.save(update_fields=["estado","documento"])

            elif request.POST["caso"]=="0":
                id= request.POST["id_c"]
                estado = request.POST["state_"+str(id)]
                if(estado=="1"):
                    comentarios=""
                elif(estado=="2"):
                    comentarios = request.FILES["comment_"+str(id)]
                documento = Documento_Adjunto.objects.get(id=id)
                documento.comentarios=comentarios
                documento.estado=estado
                documento.id_usuario=request.user
                if(comentarios==""):
                    documento.save(update_fields=["estado","id_usuario"])
                else:    
                    documento.save(update_fields=["comentarios","estado","id_usuario"])

            documentos = Documento_Adjunto.objects.filter(id_participante=participante)
            var = 0
            for documento in documentos:
                if(documento.estado=="0" or documento.estado=="2"):
                    var = 1
            participante = Participante.objects.get(id_convocatoria=convocatoria,id_semillero=semillero)
            
            if var == 0:
                participante.estado="1"
            else:
                if request.POST["caso"]=="1":
                    print("hola")
                    participante.estado="2"
                elif request.POST["caso"]=="0":    
                    participante.estado="3"

            participante.save(update_fields=["estado"])

        return render(request, "conv/adjuntos.html",{'documentos':documentos})
    return redirect('/')

def reportar(request,id):
    if request.user.groups.filter(name="Coordinador").exists():
        id_semillero = coordinadores.objects.get(user=request.user).id_semillero
        semillero = Semillero.objects.get(id=int(id_semillero))
        try:
            proyecto = Proyectos.objects.get(id=id,semillero=semillero)
            if(proyecto.estado == '1'):
                if request.method == "POST":
                    tipo = request.POST["tipo"]
                    actividades = request.POST["actividades"]
                    comprom_cump = request.POST["compro_cum"]
                    comprom_pend = request.POST["compro_pen"]
                    progreso = request.POST["progreso"]
                    #aquí se genera PDF y se guarda en documento
                    insert = Documentos_proyecto(tipo=tipo,proyecto=proyecto,documento=documento)
                    insert.save()
                    proyecto.porcentaje=progreso
                    proyecto.save(update_fields=['porcentaje'])
                    mensaje = "Se ha agregado el reporte exitosamente."
                    mensaje1 = "Exito"
                    return render(request, "conv/reporte.html",{'mensaje':mensaje,'mensaje1':mensaje1})    

                return render(request, "conv/reporte.html",{'proyecto':proyecto})
            elif(proyecto.estado == '0'):
                return redirect('/proyectos')        
        except:
            return redirect('/proyectos')
    else:
        return redirect('/proyectos')

def proyectos(request):
    if request.user.groups.filter(name="Administrador").exists():
        if request.method == 'POST':
            if request.POST['caso']=="cerrar":
                id=request.POST['id']
                proyecto = Proyectos.objects.get(id=id)
                proyecto.estado=0
                proyecto.save(update_fields=['estado'])
            
            elif request.POST["caso"]=="reabrir":
                id=request.POST['id']
                proyecto = Proyectos.objects.get(id=id)
                proyecto.estado=1
                proyecto.save(update_fields=['estado'])
                
        proyectos = Proyectos.objects.all()
        return render(request, "conv/proyectos.html",{'proyectos':proyectos})

    elif request.user.groups.filter(name="Coordinador").exists():
        id_semillero = coordinadores.objects.get(user=request.user).id_semillero
        semillero = Semillero.objects.get(id=int(id_semillero))
        proyectos = Proyectos.objects.filter(semillero=semillero)
        return render(request, "conv/proyectos.html",{'proyectos':proyectos,'semillero':semillero})
    else:
        return redirect('/')

def asignar_proyecto(request,id,id_conv):
    if request.user.groups.filter(name="Administrador").exists():
        convocatoria = Convocatoria.objects.get(id=id_conv)
        semillero = Semillero.objects.get(id=id)
        if request.method == "POST":
            try:
                codigo = request.POST["codigo"]
                proyecto = Proyectos.objects.get(codigo=codigo)
                mensaje = "Ya existe un proyecto con el codigo ingresado."
                mensaje1 = "Error"
                return render(request, "conv/asignar_proyecto.html",{'mensaje':mensaje,'mensaje1':mensaje1})
            except:    
                codigo = request.POST["codigo"]
                porcentaje = 0
                descripcion = request.POST["description"]
                start = request.POST["start"]
                closed = request.POST["closed"]
                insert = Proyectos(codigo=codigo,convocatoria=convocatoria,semillero=semillero,porcentaje=porcentaje,description=descripcion,estado="1",start=start,closed=closed)
                insert.save()
                count = int(request.POST['contador'])
                for i in range(1,count+1):
                    try:
                        proyecto=Proyectos.objects.latest('id')
                        description = request.POST['text_' + str(i)]
                        try:
                            documento = request.FILES['doc_' + str(i)]
                            insert = Documentos_proyecto_2(proyecto=proyecto, documento=documento, description=description)
                            insert.save()
                        except:
                            insert = Documentos_proyecto_2(proyecto=proyecto, description=description)
                            insert.save()
                            print("No se adjunto archivo")        
                    except:
                        print("No se puede agregar el archivo ya que fue eliminado en frontend")

                mensaje1 = "Exito"
                mensaje = "Proyecto creado exitosamente."
                return render(request, "conv/asignar_proyecto.html",{'mensaje':mensaje,'mensaje1':mensaje1})

        return render(request, "conv/asignar_proyecto.html",{'convocatoria':convocatoria,'semillero':semillero})     

    return redirect('/')

def reportes(request,id):
    if request.user.groups.filter(name="Administrador").exists():
        proyecto = Proyectos.objects.get(id=id)
        reportes = Documentos_proyecto.objects.filter(proyecto=proyecto)
        if request.method=="POST":
            id_d=request.POST["id_d"]
            reporte=Documentos_proyecto.objects.get(id=id_d)
            descripcion = request.POST["descripcion"]
            try:
                documento=request.FILES["doc"]
                insert = observaciones(reporte=reporte,documento=documento,description=descripcion)
                insert.save()
            except:
                insert = observaciones(reporte=reporte,description=descripcion)
                insert.save()

        return render(request, "conv/reportes.html",{'reportes':reportes})     
    elif request.user.groups.filter(name="Coordinador").exists():
        id_semillero = coordinadores.objects.get(user=request.user).id_semillero
        semillero = Semillero.objects.get(id=int(id_semillero))
        try:
            if request.method == "POST":
                id = request.POST["id_d"]
                reporte = Documentos_proyecto.objects.get(id=id)
                reporte.documento = request.FILES["doc"]
                reporte.save(update_fields=["documento"])
                return redirect("/proyectos")

            proyecto = Proyectos.objects.get(id=id,semillero=semillero)
            reportes = Documentos_proyecto.objects.filter(proyecto=proyecto)
            return render(request, "conv/reportes.html",{'reportes':reportes})     
        except:
            return redirect('/')
    else:
        return redirect('/')

def proyecto_details(request, id_item=None):
    if request.user.is_authenticated:
        item = Proyectos.objects.get(id=id_item)
        documentos = Documentos_proyecto_2.objects.filter(proyecto=id_item)
        return render(request, "conv/proyectos_details.html",{'item':item,'documentos':documentos})
    else:
        return redirect('/')

def proyecto_edit(request, id):
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Administrador").exists():
            proyecto = Proyectos.objects.get(id=id)
            documentos = Documentos_proyecto_2.objects.filter(proyecto=proyecto)
            if request.method=="POST":
                if request.POST['caso'] == "eliminar":
                    id = request.POST['id']
                    documento = Documentos_proyecto_2.objects.get(id=id)
                    documento.delete()
                elif request.POST['caso'] == "editar":   
                    codigo = request.POST['codigo']
                    description = request.POST['description']
                    start = request.POST['start']
                    closed = request.POST['closed']
                    proyecto=Proyectos.objects.get(id=id)
                    proyecto.codigo=codigo
                    proyecto.description=description
                    proyecto.start=start
                    proyecto.closed=closed
                    proyecto.save(update_fields=["codigo","description","start","closed"])

                    count = int(request.POST['contador'])
                    for i in range(1,count+1):
                        try:
                            convocatoria=Convocatoria.objects.latest('id')
                            description = request.POST['text_' + str(i)]
                            try:
                                documento = request.FILES['doc_' + str(i)]
                                insert = Documentos_proyecto_2(proyecto=proyecto, description=description, documento=documento)
                                insert.save()
                            except:
                                insert = Documentos_proyecto_2(proyecto=proyecto, description=description)
                                insert.save()
                                print("No se adjunto archivo")        
                        except:
                            print("No se puede agregar el archivo ya que fue eliminado en frontend")  

                    return redirect('proyectos')         

            return render(request, "conv/proyecto_edit.html",{'proyecto':proyecto,'documentos':documentos})
        else:
            return redirect('/')                
    else:
        return redirect('/')        