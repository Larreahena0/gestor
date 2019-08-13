from django.shortcuts import render
from conv.models import Convocatoria
from conv.forms import ConvocatoriaForm

# Create your views here.
def conv_create(request):
    conv_form = ConvocatoriaForm()

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        opened = request.POST['opened']
        closed = request.POST['closed']
        insert = Convocatoria(name=name, description=description, opened=opened, closed=closed)
        insert.save()
    else:
        conv_form = ConvocatoriaForm()

    return render(request, "conv/conv_create.html",{'form':conv_form})