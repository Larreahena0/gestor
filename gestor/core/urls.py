from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('sign-up', views.signup, name="sign-up")
]
