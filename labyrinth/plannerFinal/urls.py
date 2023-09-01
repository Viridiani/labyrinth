from django.urls import path
from . import views

urlpatterns = [
    path("<str:domain_name>", views.base, name="base"),
    path("", views.labyrinth, name="labyrinth")
]