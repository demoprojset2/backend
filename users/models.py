from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor_name = models.CharField(max_length=50)
    doctor_email = models.EmailField(unique=True)
    speciality = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    doctor_password = models.CharField(max_length=30)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


    def __str__(self):
        return str(self.user.username)
