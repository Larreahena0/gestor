from django.contrib import admin
from .models import Semillero
from .models import Integrante
from .models import LineaSemillero
from .models import Career
from .models import Linea
from .models import Atributos
from .models import Rol

# Register your models here.
class SemilleroAdmin(admin.ModelAdmin):
	readonly_fields = ('id', 'created', 'updated')

class LineaAdmin(admin.ModelAdmin):
	readonly_fields = ('id', 'created', 'updated')

class IntegranteAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

admin.site.register(Semillero, SemilleroAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(Linea, LineaAdmin)
admin.site.register(Career)
admin.site.register(LineaSemillero)
admin.site.register(Atributos)
admin.site.register(Rol)
