from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def participate(request):
#     convocatorias = Convocatoria.objects.all()
#     return render(request, "core/participate.html", {"convocatorias":convocatorias})
    return render(request, "core/participate.html")