from django.shortcuts import render
from workline.models import Linea
from workline.forms import LineaForm

# Create your views here.
def add_workline(request):
    linea_form = LineaForm()

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        insert = Linea(name=name, description=description)
        insert.save()
    else:
        linea_form = LineaForm()

    return render(request, "workline/add_workline.html", {'form':linea_form})