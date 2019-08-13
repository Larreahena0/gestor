from django.urls import path
from create import views

urlpatterns = [
    path('', views.create, name="create")
]