from django.contrib import admin
from .models import Grupo
from .models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Grupo)
admin.site.register(Usuario, UsuarioAdmin)