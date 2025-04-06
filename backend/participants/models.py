from django.db import models
from django.utils import timezone

# Modelo para representar a los participantes del sorteo
class Participant(models.Model):
    # Nombre del participante
    name = models.CharField(max_length=255)
    
    # Email único del participante (campo obligatorio y único)
    email = models.EmailField(unique=True)
    
    # Indica si el email del participante ha sido verificado
    is_verified = models.BooleanField(default=False)
    
    # Fecha y hora en que se creó el registro
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Fecha y hora en que se actualizó por última vez el registro
    updated_at = models.DateTimeField(auto_now=True)
    
    # Token de verificación para validar el email del participante
    verification_token = models.CharField(max_length=255, blank=True, null=True)

    # Representación en texto del modelo (usado en el panel de administración y otros lugares)
    def __str__(self):
        return self.name

    class Meta:
        # Índice en el campo email para mejorar el rendimiento en búsquedas
        indexes = [
            models.Index(fields=['email']),
        ]