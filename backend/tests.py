from django.test import TestCase
from accounts.models import User, Profile
from .models import PatientDetails, VitalDetails, Allergy, Medication, Dosage, ProblemDetails, SocialHistory, \
    PatientComments


class PatientTestCase(TestCase):
    def test_field_doctor_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        self.assertTrue(isinstance(self.doctor, Profile))

    def test_field_patient_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        self.assertTrue(isinstance(patient, PatientDetails))
        self.assertEqual(str(patient), 'Sonu')

    def test_field_VitalDetails_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        vitaldetails = VitalDetails(patient=patient, weight=75, height=147, blood_pressure=45, pulse=67,
                                    temperature=97.0)
        self.assertTrue(isinstance(vitaldetails, VitalDetails))
        self.assertEqual(str(vitaldetails), 'Sonu')

    def test_field_Allergy_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        allergy = Allergy.objects.create(patient=patient, substance="paracetamol", verification_status="Suspected",
                                         criticality="LOW", type="Allergy", comment="Issue More")
        self.assertTrue(isinstance(allergy, Allergy))
        self.assertEqual(str(allergy), 'paracetamol')

    def test_field_Medication_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M", address="Sector-49", dob="1999-09-06", phone_number="+918527879473", doctor=self.doctor)
        medication = Medication(medication_name="Dolo", medication_manufacturer="Apex", expire="2021-01-01", amount=104)
        self.assertTrue(isinstance(medication, Medication))
        self.assertEqual(str(medication), 'Dolo')

    def test_field_Dosage_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                      address="Sectro 49 Noida", dob="1999-09-06",
                                      phone_number="+918527879473", doctor=self.doctor)
        medication = Medication(medication_name="Dolo", medication_manufacturer="Apex", expire="2021-01-01", amount=104)
        dosage = Dosage(medication=medication, dose_amount=3, dose_timing="Per Day",
                        dose_description="Please take Caution")
        self.assertTrue(isinstance(dosage, Dosage))
        self.assertEqual(str(dosage), 'Dolo')

    def test_field_ProblemDetails_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        problem_detail = ProblemDetails(problem_name="Ashtma", severity="Mild", status="Active",
                                        start_date="2021-01-01", end_date="2021-01-10", patient=patient)
        self.assertTrue(isinstance(problem_detail, ProblemDetails))
        self.assertEqual(str(problem_detail), 'Ashtma')

    def test_field_SocialHistory_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name="Sonu", email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        social_history = SocialHistory(tobacco="Never Smoked", alcohol="Current drinker", patient=patient)
        self.assertTrue(isinstance(social_history), SocialHistory)
        self.assertEqual(str(social_history), 'Soun')

    def test_field_PatientComments_creation(self):
        self.user_as_doctor = User.objects.create(email='sharmasonu04359491@gmail.com')
        self.doctor = Profile.objects.create(user=self.user_as_doctor, speciality="Ortho", gender="M")
        patient = PatientDetails.objects.create(name='Sonu', email_id="sonuraj1926@gmail.com", gender="M",
                                                address="Sectro 49 Noida", dob="1999-09-06",
                                                phone_number="+918527879473", doctor=self.doctor)
        patient_comment = PatientComments(comment="Having enough Knowldge", patient=patient)
        self.assertTrue(isinstance(patient_comment, PatientComments))
        self.assertEqual(str(patient_comment), 'Sonu')
