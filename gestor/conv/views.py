from django.shortcuts import render, redirect
from .models import Convocatoria
from .models import Documento,Participante
from core.models import Grupo
from django.conf import settings
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
                    documento = request.FILES['doc_' + str(i)]
                    tipo = request.POST['sel_' + str(i)]
                    description = request.POST['text_' + str(i)]
                    insert = Documento(id_conv=convocatoria, tipo=tipo, description=description, documento=documento)
                    insert.save()
                except:
                    print("No se puede agregar el archivo ya que fue eliminado en frontend")
                    
        elif estado == 1:
            conv = Convocatoria.objects.get(id=request.POST['conv'])
            conv.delete()

    today = datetime.datetime.now()
    convocatorias = Convocatoria.objects.all()
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
                            convocatoria=Convocatoria.objects.get(id=id)
                            documento = request.FILES['doc_' + str(i)]
                            tipo = request.POST['sel_' + str(i)]
                            description = request.POST['text_' + str(i)]
                            insert = Documento(id_conv=convocatoria, tipo=tipo, description=description, documento=documento)
                            insert.save()
                        except:
                            print("No se puede agregar el archivo ya que fue eliminado en frontend")

                return redirect('participar')

            return render(request, "conv/convocatoria_edit.html",{'convocatoria': convocatoria,'documentos':documentos})

    return redirect('/')
