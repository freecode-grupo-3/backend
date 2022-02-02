# backend
Backend para la aplicación web del hackathon #freecode

## Configuraciones del Proyecto

- Entorno Virtual
    - pip install virtualenv
    - virtualenv -p python3 env
    - source env/bin/activate

- Instalar dependencias
    - Activar entorno vitual
    - pip install -r requirements.txt

- Migraciones
    - python manage.py makemigrations
    - python manage.py migrate

- Crear Super Usuario
    - python manage.py createsuperuser

- Correr servidor
    - python manage.py runserver

- Correr servidor
    - daphne -b 0.0.0.0 -p 8000 medicrumbs.asgi:application

