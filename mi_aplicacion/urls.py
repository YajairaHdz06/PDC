from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista/', views.lista.as_view(), name='milista'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('<int:pk>/editar/', views.editar_estudiante, name='editar_estudiante'),
    path('<int:pk>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('carrera/crear/', views.crear_carrera, name='crear_carrera'),
    path('carrera/', views.lista_carreras, name='lista_carreras'),
    path('carrera/<int:pk>/editar/', views.editar_carrera, name='editar_carrera'),
    path('carrera/<int:pk>/eliminar/', views.eliminar_carrera, name='eliminar_carrera'),
    path('carrera/<int:pk>/', views.detalle_carrera, name='detalle_carrera'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)