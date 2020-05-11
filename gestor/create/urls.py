from django.urls import path
from create import views

urlpatterns = [
    path('semillero/', views.create, name="create"),
    path(r'semillero/edit/<int:id>', views.semillero_edit, name="semillero_edit"),
    path(r'semillero/remove/<int:id>', views.semillero_delete, name="semillero_delete"),
    path('linea/', views.add_workline, name="workline"),
    path('integrante/', views.register, name="register"),
    path('produccion/', views.produccion, name="produccion")
]