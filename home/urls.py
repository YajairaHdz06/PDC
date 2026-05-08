from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="nosotros"),
    path("contact/", views.contact, name="contacto"),
    path("services/", views.services, name="servicios"),
    path("gallery/", views.gallery, name="galeria"),
]