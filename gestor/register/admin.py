from django.contrib import admin
from register.models import Integrante

# Register your models here.
class IntegranteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Integrante, IntegranteAdmin)