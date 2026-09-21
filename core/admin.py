from django.contrib import admin

from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "propietario", "creado")  
    search_fields = ("nombre",)  
    list_filter = ("propietario",) 

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "proyecto",
        "estado",
        "prioridad",
        "asignado_a",
        "fecha_limite",
    )
    list_filter = ("estado", "prioridad", "proyecto")
    search_fields = ("titulo",)