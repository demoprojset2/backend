from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class DoctorDetails(models.Model):
    doctor_id = models.IntegerField()
    doctor_name = models.TextField()
    doctor_email = models.TextField()
    doctor_password = models.CharField(max_length=10, validators=[MinLengthValidator(5)])

