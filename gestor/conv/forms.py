from django import forms
from conv.models import Convocatoria

class ConvocatoriaForm(forms.ModelForm):
    class Meta():
       model = Convocatoria
       fields = ['name','description','opened','closed']