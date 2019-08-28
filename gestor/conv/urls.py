from django.urls import path
from conv import views

urlpatterns = [
    path('convocatoria/', views.conv_create, name="conv_create"),
    path('participar/', views.participate, name="participate"),
    path(r'details/<int:id_item>', views.conv_details, name="details")
]
