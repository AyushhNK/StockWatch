from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Tier(models.TextChoices):
        ADMIN = "admin"
        PREMIUM = "premium"
        STANDARD = "standard"

    email = models.EmailField(unique=True)
    tier = models.CharField(
        max_length=20,
        choices=Tier.choices,
        default=Tier.STANDARD
    )
    timezone = models.CharField(max_length=50, default="UTC")
    preferred_currency = models.CharField(max_length=10, default="USD")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
