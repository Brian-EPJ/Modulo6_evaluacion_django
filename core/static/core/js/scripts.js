document.addEventListener("DOMContentLoaded", function () {

    // Agrega clases de Bootstrap a los campos que renderiza Django
    document.querySelectorAll("form input, form select, form textarea").forEach(function (campo) {
        const tipo = (campo.getAttribute("type") || "").toLowerCase();
        if (["hidden", "checkbox", "radio", "submit", "button"].includes(tipo)) {
            return;
        }
        if (campo.tagName === "SELECT") {
            campo.classList.add("form-select");
        } else {
            campo.classList.add("form-control");
        }
    });

    // Cierra las alertas de mensajes (django.contrib.messages) solas
    const alertas = document.querySelectorAll(".alert-auto-cierre");
    alertas.forEach(function (alerta) {
        setTimeout(function () {
            const instancia = bootstrap.Alert.getOrCreateInstance(alerta);
            instancia.close();
        }, 4000);
    });

    // Confirmación extra antes de eliminar
    const formEliminar = document.querySelector("[data-confirmar-eliminacion]");
    if (formEliminar) {
        formEliminar.addEventListener("submit", function (evento) {
            const mensaje = formEliminar.dataset.confirmarEliminacion;
            if (!window.confirm(mensaje)) {
                evento.preventDefault();
            }
        });
    }

    // Resalta el link activo en la barra de navegación
    const rutaActual = window.location.pathname;
    document.querySelectorAll(".navbar-app .nav-link").forEach(function (link) {
        if (link.getAttribute("href") === rutaActual) {
            link.classList.add("active", "fw-bold");
        }
    });

    // Si el formulario volvió con errores de validación, llevamos el foco
    // al primer campo con problemas para que sea fácil de encontrar.
    const primerCampoConError = document.querySelector(
        ".campo-con-error input, .campo-con-error select, .campo-con-error textarea"
    );
    if (primerCampoConError) {
        primerCampoConError.focus();
    }

});
