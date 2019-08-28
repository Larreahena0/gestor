from django.urls import path
from create import views

urlpatterns = [
    path('semillero/', views.create, name="create"),
    path('linea/', views.add_workline, name="workline"),
    path('integrante/', views.register, name="register")
]