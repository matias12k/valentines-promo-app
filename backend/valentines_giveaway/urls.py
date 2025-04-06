from django.urls import path, include
from django.contrib import admin

# Definición de las rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración

    # Incluir las rutas de la aplicación "participants"
    path('participants/', include('participants.urls')),
]