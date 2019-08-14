from django import forms
from register.models import Integrante

class DateInput(forms.DateInput):
    input_type = 'date'

class IntegranteForm(forms.ModelForm):
    class Meta():
        model = Integrante
        fields = ['name','document','semillero','rol','joined','email','career','level']

        widgets = {
            'joined': DateInput()
        }