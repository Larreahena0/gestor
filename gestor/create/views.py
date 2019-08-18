from django.shortcuts import render
from create.models import Semillero
from core.models import Grupo
from workline.models import Linea

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