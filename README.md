# 📋 Gestor de Tareas — Módulo 6

Aplicación web desarrollada con **Django** como proyecto correspondiente al **Módulo 6**, enfocada en la gestión de proyectos y tareas de forma organizada y personalizada para cada usuario.

El sistema permite a los usuarios crear y administrar sus propios proyectos, agregar tareas, asignarlas y realizar un seguimiento mediante diferentes estados, prioridades y fechas límite.

---

## 🚀 Funcionalidades

### 👤 Usuarios

* Registro de nuevos usuarios.
* Inicio y cierre de sesión.
* Autenticación mediante el sistema de usuarios de Django.
* Cada usuario puede acceder únicamente a sus propios proyectos y tareas.

### 📁 Proyectos

* Crear proyectos.
* Visualizar los proyectos propios.
* Editar proyectos.
* Eliminar proyectos.
* Asociar cada proyecto a su propietario.

### ✅ Tareas

* Crear tareas dentro de un proyecto.
* Asignar tareas a usuarios.
* Definir estado y prioridad.
* Establecer una fecha límite.
* Editar y eliminar tareas.
* Visualizar las tareas pertenecientes a los proyectos propios.

### 🛡️ Seguridad y validaciones

* Control de acceso mediante autenticación.
* Restricción de proyectos y tareas según su propietario.
* Validaciones personalizadas en formularios.
* Evita nombres de proyectos y títulos de tareas duplicados cuando corresponde.
* Validación de longitud mínima.
* La fecha límite no puede corresponder a una fecha pasada.

---

## 🛠️ Tecnologías utilizadas

* **Python**
* **Django**
* **SQLite** / base de datos configurada en el proyecto
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Django Forms**
* **Django Class-Based Views**
* **Django ORM**
* **Git & GitHub**

---

## 📂 Estructura del proyecto

```text
Gestor-de-Tareas/
│
├── django_web_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── core/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   └── core/
│   │       └── css/
│   │           └── estilos.css
│   │
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧩 Modelos principales

El proyecto trabaja principalmente con dos modelos:

### `Proyecto`

Representa un proyecto creado por un usuario.

Entre sus principales datos se encuentran:

* Nombre
* Descripción
* Propietario
* Fecha de creación

### `Tarea`

Representa una tarea perteneciente a un proyecto.

Incluye información como:

* Proyecto
* Título
* Estado
* Prioridad
* Fecha límite
* Usuario asignado

La relación entre ambos modelos permite organizar las tareas dentro de cada proyecto.

---

## 📝 Formularios y validaciones

El proyecto utiliza **Django Forms** para gestionar la entrada de información y aplicar validaciones antes de guardar los datos.

Entre las validaciones implementadas se encuentran:

* Comprobar que los nombres cumplan con una longitud mínima.
* Evitar nombres de proyectos duplicados.
* Evitar títulos de tareas duplicados cuando corresponda.
* Validar que las fechas límite sean válidas.
* Controlar los datos ingresados por el usuario antes de almacenarlos.

---

## 👨‍💻 Vistas basadas en clases

Para la lógica de las diferentes operaciones se utilizan **Class-Based Views (CBV)** de Django.

Esto permite organizar las funcionalidades de:

* Listado
* Creación
* Detalle
* Edición
* Eliminación

Además, se implementan restricciones para que un usuario no pueda acceder, modificar o eliminar proyectos y tareas que no le pertenecen.

---

## 🎨 Interfaz

La interfaz está construida utilizando **Bootstrap 5**, complementada con estilos CSS propios.

Se utiliza una paleta de colores basada en tonos grises para mantener una apariencia sencilla, limpia y consistente.

Los estilos personalizados se encuentran en:

```text
core/static/core/css/estilos.css
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Brian-EPJ/Modulo6_evaluacion_django.git
cd Modulo6_evaluacion_django
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows — PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows — CMD:**

```cmd
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

> Si PowerShell impide ejecutar `Activate.ps1`, también puedes utilizar el entorno virtual desde CMD o configurar la política de ejecución de PowerShell.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar las migraciones

```bash
python manage.py migrate
```

### 6. Crear un superusuario

Este paso es opcional y permite acceder al panel administrativo de Django.

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

Para crear una cuenta:

```text
http://127.0.0.1:8000/registro/
```

Y el panel administrativo de Django se encuentra en:

```text
http://127.0.0.1:8000/admin/
```

---

## 📌 Objetivo del proyecto

Este proyecto fue desarrollado como parte del **Módulo 6**, con el objetivo de poner en práctica conceptos fundamentales del desarrollo web utilizando Django.

Entre los principales conocimientos aplicados se encuentran:

* Creación y configuración de un proyecto Django.
* Creación de aplicaciones.
* Modelado de datos mediante Django ORM.
* Relaciones entre modelos.
* Migraciones.
* Sistema de autenticación de Django.
* Formularios y validaciones personalizadas.
* Vistas basadas en clases.
* Templates y herencia de plantillas.
* Archivos estáticos.
* Control de acceso según usuario.
* Integración de Bootstrap.
* Organización y estructura de un proyecto web.

---

## 🔐 Consideraciones para producción

El proyecto está configurado principalmente para **desarrollo local**.

Actualmente:

```python
DEBUG = True
```

Para utilizar la aplicación en un entorno de producción se recomienda:

* Cambiar `DEBUG` a `False`.
* Configurar correctamente `ALLOWED_HOSTS`.
* Utilizar una `SECRET_KEY` almacenada fuera del código fuente.
* Configurar una base de datos apropiada para producción.
* Revisar la configuración de archivos estáticos y media.
* Configurar correctamente HTTPS y las opciones de seguridad de Django.

---

## 📚 Contexto académico

**Proyecto:** Gestor de Tareas
**Módulo:** 6
**Tecnología principal:** Django / Python
**Tipo:** Aplicación web de gestión de proyectos y tareas

---

## 👨‍💻 Autor

**Brian Pradenas Jaramillo**

Proyecto desarrollado como parte del proceso de formación en desarrollo **Full Stack**, aplicando conocimientos de Python y Django en la construcción de una aplicación web funcional.

---

⭐ Si este proyecto te resulta útil o quieres revisar el código, puedes explorar el repositorio y sus diferentes componentes.
