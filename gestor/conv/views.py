from django.shortcuts import render
from .models import Convocatoria
from django.conf import settings
import os

# Create your views here.
def conv_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        opened = request.POST['opened']
        closed = request.POST['closed']

        insert = Convocatoria(name=name, description=description, opened=opened, closed=closed)
        insert.save()

        latest_conv = Convocatoria.objects.latest('id')
        os.mkdir(settings.MEDIA_ROOT + '/convocatorias/' + str(latest_conv.id))

        for count, x in enumerate(request.FILES.getlist("documents")):
            def process(f):
                with open(settings.MEDIA_ROOT + '/convocatorias/' + str(latest_conv.id) + '/' + str(x), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            process(x)

    return render(request, "conv/convocatoria.html")

def conv_details(request, id_item=None):
    item = Convocatoria.objects.get(id=id_item)
    return render(request, "conv/details.html",{'item':item})

def participate(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, "conv/participate.html",{'convocatorias':convocatorias})
