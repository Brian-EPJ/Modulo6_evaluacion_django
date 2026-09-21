from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import ProyectoForm, RegistroForm, TareaForm
from .models import Proyecto, Tarea


class RegistroView(CreateView):
    form_class = RegistroForm
    # La plantilla vive en core/templates/core/registration/registro.html,
    # así que la ruta tiene que incluir el prefijo "core/".
    template_name = "core/registration/registro.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        respuesta = super().form_valid(form)
        messages.success(
            self.request,
            "Cuenta creada correctamente. Ahora puedes iniciar sesión.",
        )
        return respuesta


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proyectos = Proyecto.objects.filter(propietario=self.request.user)
        tareas = Tarea.objects.filter(proyecto__propietario=self.request.user)

        context["proyectos"] = proyectos
        context["total_proyectos"] = proyectos.count()
        context["total_tareas"] = tareas.count()
        context["tareas_pendientes"] = tareas.filter(estado="pendiente").count()
        context["tareas_completadas"] = tareas.filter(estado="completada").count()
        return context


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = "core/proyecto_list.html"
    context_object_name = "proyectos"

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    form_class = ProyectoForm
    template_name = "core/proyecto_form.html"
    success_url = reverse_lazy("proyecto_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["propietario"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        messages.success(self.request, "Proyecto creado correctamente.")
        return super().form_valid(form)


class EsPropietarioDelProyectoMixin(UserPassesTestMixin):
    """Para vistas que reciben 'proyecto_id' en la URL (listar/crear tareas)."""

    def test_func(self):
        proyecto_id = self.kwargs.get("proyecto_id")
        proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
        return proyecto.propietario == self.request.user


class EsPropietarioDeLaTareaMixin(UserPassesTestMixin):
    """Para vistas que reciben 'pk' de una Tarea (editar/eliminar). Antes
    estas vistas no validaban dueño y cualquier usuario logueado podía
    editar o borrar tareas ajenas conociendo el ID."""

    def test_func(self):
        tarea = self.get_object()
        return tarea.proyecto.propietario == self.request.user


class TareaListView(LoginRequiredMixin, EsPropietarioDelProyectoMixin, ListView):
    model = Tarea
    template_name = "core/tarea_list.html"
    context_object_name = "tareas"

    def get_queryset(self):
        return Tarea.objects.filter(proyecto_id=self.kwargs["proyecto_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyecto"] = get_object_or_404(
            Proyecto, pk=self.kwargs["proyecto_id"]
        )
        return context


class TareaCreateView(LoginRequiredMixin, EsPropietarioDelProyectoMixin, CreateView):
    form_class = TareaForm
    template_name = "core/tarea_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["proyecto"] = get_object_or_404(Proyecto, pk=self.kwargs["proyecto_id"])
        return kwargs

    def form_valid(self, form):
        form.instance.proyecto_id = self.kwargs["proyecto_id"]
        messages.success(self.request, "Tarea creada correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "tarea_list", kwargs={"proyecto_id": self.kwargs["proyecto_id"]}
        )


class TareaUpdateView(LoginRequiredMixin, EsPropietarioDeLaTareaMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "core/tarea_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["proyecto"] = self.object.proyecto
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Tarea actualizada correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "tarea_list", kwargs={"proyecto_id": self.object.proyecto_id}
        )


class TareaDeleteView(LoginRequiredMixin, EsPropietarioDeLaTareaMixin, DeleteView):
    model = Tarea
    template_name = "core/tarea_confirm_delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Tarea eliminada correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "tarea_list", kwargs={"proyecto_id": self.object.proyecto_id}
        )
