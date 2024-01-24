# ToDoBackend API

Este es un ejemplo de README para tu proyecto ToDoBackend, una API pública desarrollada con Django Rest Framework para gestionar tareas.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/your-username/ToDoBackend.git
   cd ToDoBackend

2. **Crear un enotrno virtual (opcional, pero recomendado)**
   python-m venv venv
   source venv/bin/activate

3. **Instalar dependencias**
   pip install -r requirements.txt

4. **Realizar las migraciones de la base de datos SQLite**
   python manage.py migrate

5. **Iniciar el servidor de desarrollo**
   python manage.py runserver

Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://127.0.0.1:8000/api/tasks/ (o la URL correspondiente según tu configuración) para empezar a utilizarla.

## Uso
Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://127.0.0.1:8000/api/tasks/ (o la URL correspondiente según tu configuración). Aquí puedes realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las tareas.

La API cuenta con los siguientes endpoints:

GET /api/tasks/: Obtiene una lista de todas las tareas.
POST /api/tasks/: Crea una nueva tarea.
GET /api/tasks/<task_id>/: Obtiene detalles de una tarea específica.
PUT /api/tasks/<task_id>/: Actualiza una tarea específica.
DELETE /api/tasks/<task_id>/: Elimina una tarea específica.
## Contribuir
Si deseas contribuir a este proyecto, ¡te damos la bienvenida! Puedes hacerlo abriendo un PR (Pull Request) con tus cambios propuestos.

##Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.
