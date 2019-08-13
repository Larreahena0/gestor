from django.shortcuts import render
from create.models import Semillero
from create.forms import SemilleroForm

# Create your views here.
def create(request):
    semillero_form = SemilleroForm()

    if request.method == "POST":
        id_group = request.POST['id_group']
        name = request.POST['name']
        lines = request.POST['lines']
        insert = Semillero(id_group=id_group, name=name, lines=lines)
        insert.save()
    else:
        semillero_form = SemilleroForm()

    return render(request, "create/create.html", {'form':semillero_form})