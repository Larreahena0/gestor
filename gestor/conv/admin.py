from django.contrib import admin
from .models import Convocatoria
from .models import Documento

# Registro de los modelos convocatoria y documento, definimos también que
# sus campos id, fecha de creación y fecha de actualización son de solo-lectura.
class ConvocatoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

# Asociamos el modelo a su respectivo administrador
admin.site.register(Convocatoria, ConvocatoriaAdmin)
admin.site.register(Documento, DocumentoAdmin)
