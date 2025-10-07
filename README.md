# Cotizador Alamex - Módulo para Odoo

Este repositorio contiene el código fuente del módulo de cotizaciones para Alamex, desarrollado sobre la plataforma Odoo.

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un módulo en Odoo que permita la generación, gestión y seguimiento de cotizaciones de manera eficiente y centralizada para Alamex. Esta herramienta busca optimizar el proceso de venta, reducir los tiempos de respuesta a clientes y estandarizar la presentación de las cotizaciones.

---

## 🏁 Versión 1.0: Hitos y Metas

La versión 1.0 se enfoca en establecer las bases fundamentales del módulo, creando la estructura inicial y las funcionalidades esenciales para la creación de cotizaciones.

### Objetivos Principales:

* **Estructura de Carpetas:** Creación de la estructura de directorios estándar para un módulo de Odoo, incluyendo `models`, `views`, `controllers`, `static`, etc.
* **Módulo en Odoo:** Desarrollo del módulo inicial instalable en una instancia de Odoo.
* **Modelo de Datos:** Definición de los modelos de datos principales para las cotizaciones, incluyendo campos para cliente, productos, precios, términos y condiciones.
* **Vista de Formulario de Cotización:** Diseño e implementación de la vista de formulario principal que permitirá a los usuarios crear y editar cotizaciones de manera intuitiva.
* **Vistas Básicas:** Desarrollo de las vistas de lista (tree) y de búsqueda para facilitar la localización y gestión de las cotizaciones existentes.

---

## 📂 Estructura del Módulo

El proyecto sigue la estructura estándar de un módulo de Odoo:
alamex_cotizador/
├── init.py
├── manifest.py
├── controllers/
│   ├── init.py
│   └── main.py
├── models/
│   ├── init.py
│   └── cotizacion.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── description/
│       └── icon.png
└── views/
└── cotizacion_views.xml

---

## 🚀 Instalación y Puesta en Marcha

Para instalar este módulo en tu instancia de Odoo, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone <xxxxxxxx>
    ```
2.  **Mueve el módulo a tu carpeta de `addons`:**
    Copia la carpeta `alamex_cotizador` a la carpeta donde tienes tus módulos personalizados de Odoo.

3.  **Reinicia el servicio de Odoo:**
    Asegúrate de reiniciar el servidor de Odoo para que reconozca el nuevo módulo.

4.  **Activa el modo de desarrollador:**
    En la interfaz de Odoo, ve a `Ajustes` y activa el "Modo de desarrollador".

5.  **Instala el módulo:**
    Ve a `Aplicaciones`, busca "Cotizador Alamex" y haz clic en "Instalar".

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, Odoo Framework
* **Frontend:** XML, JavaScript (a través de Odoo)
* **Base de Datos:** PostgreSQL

---

## 🤝 Contribuciones

Por el momento, el desarrollo está a cargo del equipo interno. Más adelante se definirán guías para contribuciones externas.

---

## 📝 Licencia

Este proyecto es propiedad de Alamex y su uso y distribución están restringidos.

---

**¡Gracias por ser parte de este proyecto!** 🎉
