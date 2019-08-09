from django.contrib import admin
from .models import Semillero, Integrante, Linea, Convocatoria

# Register your models here.
class SemilleroAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class IntegranteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class LineaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class ConvocatoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Semillero, SemilleroAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(Linea, LineaAdmin)
admin.site.register(Convocatoria, ConvocatoriaAdmin)
