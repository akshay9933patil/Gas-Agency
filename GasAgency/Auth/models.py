from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomerUserManager(UserManager):
    def create_customer_representative(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)
    

class Customer(AbstractUser):
    address = models.CharField(max_length=255)

    objects = CustomerUserManager()

    def __str__(self):
        return self.username
    

class CustomerRepresentative(Customer):
    objects = CustomerUserManager()

    def __str__(self):
        return self.email


Customer._meta.get_field('groups').remote_field.related_name = 'customer_groups'
Customer._meta.get_field('user_permissions').remote_field.related_name = 'customer_user_permissions'

CustomerRepresentative._meta.get_field('groups').remote_field.related_name = 'customer_representative_groups'
CustomerRepresentative._meta.get_field('user_permissions').remote_field.related_name = 'customer_representative_user_permissions'
