from django.db.models import fields
from rest_framework import serializers
from .models import *

class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = '__all__'

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'

class VitalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalDetails
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class DosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosage
        fields = '__all__'

class ProblemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemDetails
        fields = '__all__'
    
class SocialHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialHistory
        fields = '__all__'

class SimpleProblemPatient(serializers.ModelSerializer):
    class Meta:
        model = ProblemDetails
        fields = ['id', 'problem_name', 'start_date', 'end_date']

class SimpleDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = ['id', 'doctor_name', 'speciality']

class PatientDeshboardSerializer(serializers.ModelSerializer):
    doctor = SimpleDoctorSerializer()
    problem_patient = SimpleProblemPatient(many=True)

    class Meta:
        model = PatientDetails
        fields = ['doctor', 'problem_patient']


