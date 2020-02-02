from django.contrib import admin
from .models import Grupo
from .models import Usuario
from .models import Noticia

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Grupo)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Noticia, NoticiaAdmin)