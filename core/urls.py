from django.urls import path

from .views import (
    DashboardView,
    ProyectoCreateView,
    ProyectoListView,
    TareaCreateView,
    TareaDeleteView,
    TareaListView,
    TareaUpdateView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("proyectos/", ProyectoListView.as_view(), name="proyecto_list"),
    path("proyectos/nuevo/", ProyectoCreateView.as_view(), name="proyecto_create"),
    path(
        "proyectos/<int:proyecto_id>/tareas/",
        TareaListView.as_view(),
        name="tarea_list",
    ),
    path(
        "proyectos/<int:proyecto_id>/tareas/nueva/",
        TareaCreateView.as_view(),
        name="tarea_create",
    ),
    path("tareas/<int:pk>/editar/", TareaUpdateView.as_view(), name="tarea_update"),
    path("tareas/<int:pk>/eliminar/", TareaDeleteView.as_view(), name="tarea_delete"),
]
