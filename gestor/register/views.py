from django.shortcuts import render
from register.models import Integrante
from register.forms import IntegranteForm

# Create your views here.
def register(request):
    integrante_form = IntegranteForm()

    if request.method == "POST":
        name = request.POST['name']
        document = request.POST['document']
        rol = request.POST['rol']
        joined = request.POST['joined']
        email = request.POST['email']
        career = request.POST['career']
        level = request.POST['level']
        insert = Integrante(name=name, document=document, rol=rol, joined=joined, email=email, career=career, level=level)
        insert.save()
    else:
        integrante_form = IntegranteForm()

    return render(request, "register/register.html", {'form':integrante_form})