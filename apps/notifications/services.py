from .models import Notification


def send_notification(user, message):
    send_in_app(user, message)
    send_email(user, message)
    send_webhook(user, message)


def send_in_app(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )


def send_email(user, message):
    
    print(f"[EMAIL] To: {user.email} | {message}")


def send_webhook(user, message):
    
    print(f"[WEBHOOK] User={user.id} | {message}")
