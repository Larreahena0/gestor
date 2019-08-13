from django.contrib import admin
from create.models import Semillero

# Register your models here.
class SemilleroAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(Semillero, SemilleroAdmin)