from django.contrib import admin
from .models import Participant

# Registro del modelo Participant en el panel de administración de Django
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de participantes en el panel de administración
    list_display = ('name', 'email', 'is_verified', 'created_at')
    
    # Campos por los que se puede buscar en el panel de administración
    search_fields = ('name', 'email')
    
    # Filtros disponibles en el panel de administración
    list_filter = ('is_verified',)
    
    # Orden predeterminado de los registros (por fecha de creación en orden descendente)
    ordering = ('-created_at',)