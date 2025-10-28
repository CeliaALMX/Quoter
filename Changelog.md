# Changelog

Este archivo documenta todos los cambios relevantes realizados en el proyecto.  
El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y sigue las convenciones de [SemVer](https://semver.org/lang/es/).

## [Unreleased]
### Changes
- Funcionalidades planificadas o en desarrollo para próximas versiones.

---

## [1.0.0] - 2025-07-01
### Initial Release
- Versión inicial del sistema de tickets con autenticación de empleados.
- Configuración base de roles, permisos y estructura principal del módulo.
---


## [1.1.0] - 2025-10-21
### Added
- Nueva función para importar datos sin necesidad de reiniciar el servidor.
- Asociación automática del campo usuario_id al modelo de empleados.
- Se agrego una barra de estado con un "widget".
  

### Changed
- Actualización de la lógica de permisos en el modelo *helpdesk.ticket*.
- Optimización del rendimiento en la carga de vistas tridimensionales.
- El campo de altura, se modificó para hacer que reciba números decimales.
- Eliminamos el campo de ancho de puerta debido a que estaba duplicado.


### Fixed
- Corrección del error que afectaba la visibilidad de los tickets del administrador.
- Resolución del problema con botones invisibles en el modelo 3D de ascensores.
- Agregamos un botón llamado "enviar cotización".
- Agregamos un botón de "confirmar", el cual manda y cambia la barra de estado a confirmada.

  
### Removed
- Eliminación de funciones obsoletas del módulo `legacy_helpdesk`.
-- El campo de grupo de elevadores, se eliminó con la terminación x con todos los campos.
  
---

## [1.2.0] - 2025-10-16
### Arded
- Implementación de variantes de productos en el módulo de inventario.
- Implementamos un campo de folio, el cual va con la siguiente nomenclatura "COT/ALAM/0000", donde COT es cotización, ALAM es Alamex, el nombre de la empresa, 0000 son los números de cotizaciones.
- Se agrega un botón con el que se pretende generar un pdf. PERO NO SE HA TERMINADO DE CODIFICAR, QUEDA PENDIENTE.
- Se agrega un campo el cual es el primero que se debe llenar y es TIPO DE CABINA.


### Changad
- Ajustes en las vistas XML para mejorar la compatibilidad con dispositivos móviles.
- Se ajusto la vista para una mejor comprensión.
- Se bloqueo la función de edición de campos cuando la cotización este en el estado de CONFIRMADA.

  
### Removed
- Se depuro el código, con la finalidad de eliminar todos los campos y funciones redundantes.
- Se elimino el campo de compañía en el grupo de dimensiones del cubo y componentes.
---


## [1.2.2] -2025-10-27
### Added
- Se termino de codificar el botón que crea pdfs.
- Se agrego la función que muestra un título en el pdf generado.
- Se agrego la función que jala y muestra los datos generales del cliente en el pdf.
- Se crearon dos nuevos archivos en donde se diseñará y se codificará el pdf. Llamados guiamecanica_pdf.py y guiamecanica_pdf.xml.
   

### Changad
- Se ajusto la vista del pdf generado para una mejor comprensión.



### Removed
- Se depuraron errores.

## Instrucciones para colaboradores

Para mantener un historial claro y uniforme de los cambios realizados, siga las siguientes indicaciones:

1. **Crear una nueva sección** bajo `[Unreleased]` o una nueva versión cuando se haga un lanzamiento.
2. Clasifique los cambios utilizando las siguientes categorías:
   - **Added:** Para nuevas funcionalidades.
   - **Changed:** Para modificaciones en comportamiento existente.
   - **Fixed:** Para correcciones de errores.
   - **Removed:** Para eliminaciones de funcionalidades o componentes.
3. Incluya fechas en formato **YYYY-MM-DD** cuando se libere una nueva versión.
4. Use un tono técnico, objetivo y sin abreviaturas informales.
5. Evite incluir detalles internos o confidenciales; solo describa el resultado o impacto del cambio.

