from django.shortcuts import render
from register.models import Integrante
from create.models import Semillero

# Create your views here.
def register(request):

    semilleros = Semillero.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        document = request.POST['document']
        semillero = request.POST['semillero']
        rol = request.POST['rol']
        joined = request.POST['joined']
        email = request.POST['email']
        career = request.POST['career']
        level = request.POST['level']
        insert = Integrante(name=name, document=document, semillero=semillero, rol=rol, joined=joined, email=email, career=career, level=level)
        insert.save()

    return render(request, "register/register.html",{'semilleros':semilleros})