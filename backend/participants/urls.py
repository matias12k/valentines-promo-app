from django.urls import path
from .views import (
    RegisterView,
    VerifyEmailView,
    SetPasswordView,
    AdminLoginView,
    SelectWinnerView,
)

# Definición de las rutas para los endpoints de la aplicación
urlpatterns = [
    # Ruta para registrar un nuevo participante
    path('register/', RegisterView.as_view(), name='register'),
    
    # Ruta para verificar el email del participante usando un token
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    
    # Ruta para que el participante establezca su contraseña
    path('set-password/<str:token>/', SetPasswordView.as_view(), name='set_password'),
    
    # Ruta para el inicio de sesión del administrador
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    
    # Ruta protegida para que el administrador seleccione un ganador aleatorio
    path('admin/select-winner/', SelectWinnerView.as_view(), name='select_winner'),
]