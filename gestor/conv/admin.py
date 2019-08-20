from django.contrib import admin
from .models import Convocatoria
from .models import Documento

# Register your models here.
class ConvocatoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Convocatoria, ConvocatoriaAdmin)
admin.site.register(Documento, DocumentoAdmin)
