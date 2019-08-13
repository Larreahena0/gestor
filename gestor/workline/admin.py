from django.contrib import admin
from workline.models import Linea

# Register your models here.
class LineaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Linea, LineaAdmin)