# Changelog

Este archivo documenta todos los cambios relevantes realizados en el proyecto.  
El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y sigue las convenciones de [SemVer](https://semver.org/lang/es/).

## [Unreleased]
### Changes
- Funcionalidades planificadas o en desarrollo para próximas versiones.

---

## [1.1.0] - 2025-10-21
### Added
- Nueva función para importar datos sin necesidad de reiniciar el servidor.
- Asociación automática del campo usuario_id al modelo de empleados.
- Se agrego una barra de estado con un "widget".
  

### Changed
- Actualización de la lógica de permisos en el modelo *helpdesk.ticket*.
- Optimización del rendimiento en la carga de vistas tridimensionales.
- El campo de altura, se modifico para hacer que reciba números decimales.
- Eliminamos el campo de ancho de puerta debido a que estaba duplicado.

### Fixed
- Corrección del error que afectaba la visibilidad de los tickets del administrador.
- Resolución del problema con botones invisibles en el modelo 3D de ascensores.
- Agregamos un boton llamado "enviar cotizacion".
- Agregamos un boton de "confirmar", el cual manda y cambia la barra de estado a confirmada.
  
### Removed
- Eliminación de funciones obsoletas del módulo `legacy_helpdesk`.
-- El campo de grupo de elevadores, se elimino con la terminacón x con todos los campos.
  
---

## [1.2.0] - 2025-10-16
### Added
- Implementación de variantes de productos en el módulo de inventario.
- 

### Changed
- Ajustes en las vistas XML para mejorar la compatibilidad con dispositivos móviles.

---

## [1.0.0] - 2025-07-01
### Initial Release
- Versión inicial del sistema de tickets con autenticación de empleados.
- Configuración base de roles, permisos y estructura principal del módulo.

---

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

