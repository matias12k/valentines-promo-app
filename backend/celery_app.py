from celery import Celery
import os

# Establecer la configuración predeterminada del módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentines_giveaway.settings')

# Crear una instancia de la aplicación Celery
app = Celery('valentines_giveaway')

# Cargar la configuración desde el archivo de configuración de Django
# Usando el prefijo 'CELERY_' para las variables relacionadas con Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir automáticamente las tareas definidas en las aplicaciones registradas
app.autodiscover_tasks()