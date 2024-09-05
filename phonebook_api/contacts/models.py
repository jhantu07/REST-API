from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    contacts = models.ManyToManyField('self', through='Contact', symmetrical=False)

    # Override related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True
    )

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contacts')
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_spam = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'phone_number')
