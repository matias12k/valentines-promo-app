from django.apps import AppConfig

# Configuración de la aplicación "participants"
class ParticipantsConfig(AppConfig):
    # Tipo de campo automático predeterminado para los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación
    name = 'participants'