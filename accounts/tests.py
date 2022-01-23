from django.test import TestCase
from .models import User,Profile
# Create your tests here.
class DoctorTestCase(TestCase):
    def test_field_doctor_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        self.assertTrue(isinstance(self.doctor, Profile))