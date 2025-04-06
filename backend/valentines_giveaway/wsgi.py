import os
from django.core.wsgi import get_wsgi_application

# Establecer la configuración predeterminada del módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentines_giveaway.settings')

# Obtener la aplicación WSGI para el proyecto
application = get_wsgi_application()