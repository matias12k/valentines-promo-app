from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView  # Import necesario para AdminLoginView
from django.contrib.auth import authenticate  # Import necesario para autenticar usuarios
from django.utils.crypto import get_random_string
from .models import Participant
from .serializers import ParticipantSerializer, ParticipantVerificationSerializer
from .tasks import send_verification_email
import random

# Vista para registrar un nuevo participante
class RegisterView(generics.CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def perform_create(self, serializer):
        # Verificar si el email ya está registrado
        email = serializer.validated_data['email']
        if Participant.objects.filter(email=email).exists():
            return Response({"error": "Email already registered."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generar un token de verificación y guardar el participante
        token = get_random_string(length=32)
        serializer.save(verification_token=token, is_verified=False)
        
        # Enviar el email de verificación de forma asincrónica
        send_verification_email.delay(email, token)

# Vista para verificar el email del participante
class VerifyEmailView(generics.GenericAPIView):
    serializer_class = ParticipantVerificationSerializer

    def post(self, request, token):
        try:
            # Buscar al participante por el token de verificación
            participant = Participant.objects.get(verification_token=token)
            participant.is_verified = True  # Marcar como verificado
            participant.verification_token = ''  # Limpiar el token
            participant.save()
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        except Participant.DoesNotExist:
            # Manejar el caso de un token inválido
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

# Vista para que el participante establezca su contraseña
class SetPasswordView(generics.UpdateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantVerificationSerializer

    def patch(self, request, *args, **kwargs):
        # Obtener el participante y establecer la contraseña
        participant = self.get_object()
        participant.set_password(request.data['password'])
        participant.save()
        return Response({"message": "Password set successfully."}, status=status.HTTP_200_OK)

class AdminLoginView(APIView):
    def get(self, request):
        return Response({"message": "GET method is not implemented for this endpoint"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Verifica que sea un administrador
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
# Vista para seleccionar un ganador aleatorio
class SelectWinnerView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    def post(self, request):
        # Obtener todos los participantes verificados
        verified_participants = Participant.objects.filter(is_verified=True)
        if not verified_participants.exists():
            # Manejar el caso en que no haya participantes verificados
            return Response({"error": "No verified participants."}, status=status.HTTP_400_BAD_REQUEST)

        # Seleccionar un ganador aleatorio
        winner = random.choice(verified_participants)
        
        # Lógica para enviar un email al ganador (puede implementarse en tasks.py)
        return Response({"message": f"The winner is {winner.name}!"}, status=status.HTTP_200_OK)