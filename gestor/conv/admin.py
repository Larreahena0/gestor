from django.contrib import admin
from conv.models import Convocatoria

# Register your models here.
class ConvocatoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Convocatoria, ConvocatoriaAdmin)