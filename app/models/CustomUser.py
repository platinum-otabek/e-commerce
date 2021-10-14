from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    PRODUCT_OWNER = 'product_owner'
    ADMIN = 'admin'
    USER_CHOICES = (
        (CUSTOMER, 'customer'),
        (PRODUCT_OWNER, 'product_owner'),
        (ADMIN, 'admin')
    )

    role_users = models.CharField(max_length=50, choices=USER_CHOICES)
    phone_number = models.CharField(max_length=13, null=True, blank=True)


