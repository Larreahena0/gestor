from django import forms
from workline.models import Linea

class LineaForm(forms.ModelForm):
    class Meta():
       model = Linea
       fields = ['name','description']