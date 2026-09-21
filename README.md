# Gestor de Tareas

Aplicación web en Django para administrar proyectos y sus tareas: cada usuario
ve solo sus propios proyectos, puede crear tareas dentro de ellos, asignarlas,
marcarles estado/prioridad y fecha límite.

## Cómo correrlo

```bash
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # opcional, para entrar a /admin/
python manage.py runserver
```

Después entrá a `http://127.0.0.1:8000/registro/` para crear una cuenta.

## Estructura

- `django_web_app/` — configuración del proyecto (settings, urls).
- `core/` — la app con modelos, vistas, formularios y templates.
  - `models.py` — `Proyecto` y `Tarea`.
  - `forms.py` — formularios con validaciones propias (nombres/títulos
    duplicados, longitud mínima, fecha límite no puede ser pasada).
  - `views.py` — vistas basadas en clases; cada proyecto/tarea solo puede
    ser visto/editado por su dueño.
  - `templates/` — HTML con Bootstrap 5 y una paleta de colores gris propia
    (`core/static/core/css/estilos.css`).

## Notas

- `DEBUG = True` está pensado para desarrollo local. Para producción hay que
  ponerlo en `False`, completar `ALLOWED_HOSTS` y configurar una `SECRET_KEY`
  fuera del código fuente.
- Con `DEBUG = False` se muestran las páginas de error personalizadas
  (`404.html`, `403.html`, `500.html`) en vez de la página de debug de Django.
