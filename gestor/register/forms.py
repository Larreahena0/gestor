from django import forms
from register.models import Integrante

class IntegranteForm(forms.ModelForm):
    class Meta():
        model = Integrante
        fields = ['name','document','rol','joined','email','career','level']