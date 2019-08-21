from django.shortcuts import render
from .models import Convocatoria
from .models import Documento
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
            print('doc_' + str(i))
            description = request.POST['text_' + str(i)]

            insert = Documento(id_conv=id_conv, description=description, documento=documento)
            insert.save()

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    return render(request, "conv/convocatoria.html",{'today':today})

def conv_details(request, id_item=None):
    item = Convocatoria.objects.get(id=id_item)
    documents = Documento.objects.filter(id_conv=id_item)
    return render(request, "conv/details.html",{'item':item,'documents':documents,})

def participate(request):
    today = datetime.datetime.now()
    convocatorias = Convocatoria.objects.all()
    print(convocatorias)
    return render(request, "conv/participate.html",{'convocatorias':convocatorias,'today':today})
