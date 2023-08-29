from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.base, name="base"),
    path("", views.labyrinth, name="labyrinth")
]