from django.urls import path
from workline import views

urlpatterns = [
    path('', views.add_workline, name="workline")
]
