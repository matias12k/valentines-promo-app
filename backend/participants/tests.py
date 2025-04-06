from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Participant

# Clase de pruebas para los endpoints relacionados con los participantes
class ParticipantTests(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.client = APIClient()
        self.participant_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'personal_data': 'Some personal data'
        }
        self.verification_token = 'test-token'

    # Prueba para registrar un nuevo participante
    def test_register_participant(self):
        response = self.client.post(reverse('participant-register'), self.participant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Verifica que el registro sea exitoso
        self.assertEqual(Participant.objects.count(), 1)  # Verifica que se haya creado un participante
        self.assertEqual(Participant.objects.get().email, 'john.doe@example.com')  # Verifica el email registrado

    # Prueba para evitar registros duplicados con el mismo email
    def test_register_participant_email_already_exists(self):
        self.client.post(reverse('participant-register'), self.participant_data)
        response = self.client.post(reverse('participant-register'), self.participant_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Verifica que se retorne un error

    # Prueba para verificar el email de un participante
    def test_verify_email(self):
        participant = Participant.objects.create(**self.participant_data, is_verified=False)
        response = self.client.post(reverse('participant-verify', args=[self.verification_token]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica que la verificación sea exitosa
        participant.refresh_from_db()
        self.assertTrue(participant.is_verified)  # Verifica que el participante esté marcado como verificado

    # Prueba para establecer una contraseña para un participante
    def test_set_password(self):
        participant = Participant.objects.create(**self.participant_data, is_verified=True)
        response = self.client.post(reverse('participant-set-password', args=[participant.id]), {'password': 'newpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica que la contraseña se haya establecido
        participant.refresh_from_db()
        self.assertTrue(participant.check_password('newpassword'))  # Verifica que la contraseña sea correcta

    # Prueba para el inicio de sesión del administrador
    def test_admin_login(self):
        # Supone que existe un usuario administrador creado para las pruebas
        response = self.client.post(reverse('admin-login'), {'username': 'admin', 'password': 'adminpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica que el inicio de sesión sea exitoso

    # Prueba para seleccionar un ganador aleatorio
    def test_select_winner(self):
        # Crear participantes verificados
        for i in range(5):
            Participant.objects.create(name=f'Participant {i}', email=f'participant{i}@example.com', is_verified=True)
        
        response = self.client.post(reverse('select-winner'), HTTP_AUTHORIZATION='Bearer test-admin-token')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica que la selección sea exitosa
        self.assertIn('winner', response.data)  # Verifica que se incluya el ganador en la respuesta