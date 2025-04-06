from celery import shared_task

@shared_task
def send_verification_email(email, token):
    # Lógica para enviar el correo electrónico de verificación
    print(f"Enviando correo de verificación a {email} con token {token}")