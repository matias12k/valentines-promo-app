from rest_framework import serializers
from .models import Participant

# Serializer para mostrar información básica del participante
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        # Campos que se incluirán en la representación del participante
        fields = ['id', 'name', 'email', 'is_verified', 'created_at']
        # Campos que serán de solo lectura
        read_only_fields = ['id', 'is_verified', 'created_at']

# Serializer para el registro de nuevos participantes
class ParticipantRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        # Campos requeridos para el registro
        fields = ['name', 'email']
    
    # Validación personalizada para verificar si el email ya está registrado
    def validate_email(self, value):
        if Participant.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

# Serializer para la verificación del participante y creación de contraseña
class ParticipantVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        # Campo requerido para establecer la contraseña
        fields = ['password']
        # Configuración adicional para que la contraseña sea de solo escritura
        extra_kwargs = {'password': {'write_only': True}}

    # Método para actualizar el participante (establecer contraseña y marcar como verificado)
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])  # Establecer la contraseña
        instance.is_verified = True  # Marcar como verificado
        instance.save()  # Guardar los cambios en la base de datos
        return instance