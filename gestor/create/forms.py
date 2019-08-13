from django import forms
from create.models import Semillero

class SemilleroForm(forms.ModelForm):
    class Meta():
       model = Semillero
       fields = ['id_group','name','lines']