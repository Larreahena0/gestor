from django.urls import path
from conv import views

urlpatterns = [
    # Enlaces estaticos a las paginas para crear convocatoria y participar
    path('convocatoria/', views.conv_create, name="conv_create"),
    path('participar/', views.participar, name="participar"),
    path(r'participar/edit/<int:id>', views.convocatoria_edit, name="convocatoria_edit"),
    # Enlace dinamico para ver la información de la convocatoria,
    # Es posible acceder definiendo el id de la convocatoria
    path(r'details/<int:id_item>', views.conv_details, name="details")
]
