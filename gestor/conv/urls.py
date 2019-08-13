from django.urls import path
from conv import views

urlpatterns = [
    path('', views.conv_create, name="conv_create")
]