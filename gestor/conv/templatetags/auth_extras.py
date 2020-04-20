from django import template

register = template.Library()

@register.filter(name="is_admin")
def is_admin(user):
    return user.groups.filter(name="Administrador").exists()

@register.filter(name="is_coord")
def is_coord(user):
    return user.groups.filter(name="Coordinador").exists()