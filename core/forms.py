from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Proyecto, Tarea


class RegistroForm(UserCreationForm):
    """Registro de usuario, agregando correo electrónico obligatorio y
    validando que no se repita entre cuentas."""

    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        help_text="Lo vamos a usar solo para identificar tu cuenta.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con ese correo electrónico.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]
        if commit:
            usuario.save()
        return usuario


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, propietario=None, **kwargs):
        # El propietario se usa para validar que no repita el nombre de
        # proyecto; lo inyecta la vista, no viene del formulario.
        self.propietario = propietario
        super().__init__(*args, **kwargs)

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_descripcion(self):
        return self.cleaned_data.get("descripcion", "").strip()

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        if nombre and self.propietario:
            duplicados = Proyecto.objects.filter(
                propietario=self.propietario, nombre__iexact=nombre
            )
            if self.instance.pk:
                duplicados = duplicados.exclude(pk=self.instance.pk)
            if duplicados.exists():
                self.add_error("nombre", "Ya tenés un proyecto con ese nombre.")
        return cleaned_data


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "estado", "prioridad", "fecha_limite", "asignado_a"]
        widgets = {
            "fecha_limite": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, proyecto=None, **kwargs):
        # El proyecto se usa para validar que no se repita el título de
        # tarea dentro del mismo proyecto; lo inyecta la vista.
        self.proyecto = proyecto
        super().__init__(*args, **kwargs)

    def clean_titulo(self):
        titulo = self.cleaned_data.get("titulo", "").strip()
        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get("fecha_limite")
        if fecha_limite and fecha_limite < date.today():
            raise forms.ValidationError(
                "La fecha límite no puede ser anterior a hoy."
            )
        return fecha_limite

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get("titulo")
        if titulo and self.proyecto:
            duplicadas = Tarea.objects.filter(
                proyecto=self.proyecto, titulo__iexact=titulo
            )
            if self.instance.pk:
                duplicadas = duplicadas.exclude(pk=self.instance.pk)
            if duplicadas.exists():
                self.add_error("titulo", "Ya existe una tarea con ese título en este proyecto.")
        return cleaned_data
