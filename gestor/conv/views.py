from django.shortcuts import render
from .models import Convocatoria
from .models import Documento
from core.models import Grupo
from django.conf import settings
import datetime

# Create your views here.
def conv_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        opened = request.POST['opened']
        closed = request.POST['closed']

        insert = Convocatoria(name=name, description=description, opened=opened, closed=closed)
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

    return render(request, "conv/convocatoria.html",{'today':today})

def conv_details(request, id_item=None):
    grupos = Grupo.objects.all()
    today = datetime.datetime.now()
    item = Convocatoria.objects.get(id=id_item)
    inf_documents = Documento.objects.filter(id_conv=id_item,tipo=1)
    opc_documents = Documento.objects.filter(id_conv=id_item,tipo=2)
    obl_documents = Documento.objects.filter(id_conv=id_item,tipo=3)
    return render(request, "conv/details.html",{'grupos':grupos,'item':item,'inf_documents':inf_documents,'opc_documents':opc_documents,
        'obl_documents':obl_documents,'today':today,})

def participate(request):
    today = datetime.datetime.now()
    convocatorias = Convocatoria.objects.all()
    return render(request, "conv/participate.html",{'convocatorias':convocatorias,'today':today})
