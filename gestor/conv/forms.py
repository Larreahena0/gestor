from django import forms
from conv.models import Convocatoria

class DateInput(forms.DateInput):
    input_type = 'date'

class ConvocatoriaForm(forms.ModelForm):
    class Meta():
       model = Convocatoria
       fields = ['name','description','opened','closed']

       widgets = {
            'opened': DateInput(),
            'closed': DateInput(),
        }