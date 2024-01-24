# ToDoBackend API

Este es un ejemplo de README para tu proyecto ToDoBackend, una API pública desarrollada con Django Rest Framework para gestionar tareas.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Emiliooo90/ToDoBackend.git
   cd ToDoBackend

2. **Crear un enotrno virtual (opcional, pero recomendado)**
   ```bash
   python-m venv venv
   source venv/bin/activate

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt

6. **Realizar las migraciones de la base de datos SQLite**
   ```bash
   python manage.py migrate

8. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver

Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://127.0.0.1:8000/api/tareas/ (o la URL correspondiente según tu configuración) para empezar a utilizarla.

## Documentación
Toda la documentación necesaria la puedes encontrar en los siguientes endpoints http://127.0.0.1:8000/api/swagger/ y http://127.0.0.1:8000/api/redoc/

## Uso
Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://127.0.0.1:8000/api/tareas/ (o la URL correspondiente según tu configuración). Aquí puedes realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las tareas.

La API cuenta con los siguientes endpoints:

GET /api/tareas/: Obtiene una lista de todas las tareas.
POST /api/tareas/: Crea una nueva tarea.
GET /api/tareas/<task_id>/: Obtiene detalles de una tarea específica.
PUT /api/tareas/<task_id>/: Actualiza una tarea específica.
DELETE /api/tareas/<task_id>/: Elimina una tarea específica.
## Contribuir
Si deseas contribuir a este proyecto, ¡te damos la bienvenida! Puedes hacerlo abriendo un PR (Pull Request) con tus cambios propuestos.

## Licencia
Este proyecto esta bajo la licencia de Emilio Romero.
