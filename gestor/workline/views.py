from django.shortcuts import render
from .models import Linea

# Create your views here.
def add_workline(request):

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        insert = Linea(name=name, description=description)
        insert.save()

    return render(request, "workline/workline.html")
