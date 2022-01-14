from django.db.models.fields import UUIDField
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from itsdangerous import serializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
# from .serializers import DoctorDetailSerializer
from .models import DoctorDetails, Medication, PatientDetails, SocialHistory, VitalDetails
import uuid
from .serializers import DoctorDetailsSerializer, MedicationSerializer, PatientDetailsSerializer, SocialHistorySerializer, VitalDetailsSerializer, PatientDeshboardSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.views import APIView


class DoctorViewSet(ModelViewSet):
    queryset = DoctorDetails.objects.all()
    serializer_class = DoctorDetailsSerializer
        
    @action(methods=['get'], detail=True)
    def me(self, request, *args, **kwargs):
        target_user = uuid.UUID(kwargs['doctorid'])
        try:
            doctor = DoctorDetails.objects.get(id=target_user)
            serializer = DoctorDetailsSerializer(doctor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientAddViewSet(ModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

    def addpatient(self, request, *args, **kwargs):
        serializer = PatientDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientViewSet(APIView):  
    def get(self, request,doctorid,patientid):
        serializer_class = PatientDetailsSerializer
        patientid = uuid.UUID(patientid)
        patient = None
        try:
            patient = PatientDetails.objects.get(id=patientid)
            return Response(PatientDetailsSerializer(patient).data,status=status.HTTP_200_OK)
        except:
            content = {'Patient does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    # def post(self, request, doctorid):
    #     serializer_class = PatientDetailsSerializer
    #     serializer = PatientDetailsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, doctorid, patientid):
        serializer_class = PatientDetailsSerializer
        patientid = uuid.UUID(patientid)
        patient = None
        try:
            patient = PatientDetails.objects.get(id=patientid)
            serializer = PatientDetailsSerializer(patient, data=request.data)
            # print(vitaldetails)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            content = {'Patient does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
    
class VitalsViewSet(ModelViewSet):
    queryset = VitalDetails.objects.all()
    serializer_class = VitalDetailsSerializer

    @action(methods=['post'], detail=True)
    def addvitals(self, request, *args, **kwargs):
        target_user = uuid.UUID(kwargs['doctorid'])
        serializer = VitalDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicationViewSet(ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    @action(methods=['get','post'], detail=True)
    def meds(self, request, *args, **kwargs):
        if request.method == 'GET':
            target_user = uuid.UUID(kwargs['patientid'])
            print(target_user)
            try:
                patient = PatientDetails.objects.get(id=target_user)
                meds = Medication.objects.get(patient=patient)
                serializer = MedicationSerializer(meds)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                content = {"Not found"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = MedicationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class SocialViewSet(APIView):
    def get(self, request, patientid):
        serializer_class = SocialHistorySerializer
        patientid = uuid.UUID(patientid)
        patient = None
        try:
            patient = PatientDetails.objects.get(id=patientid)
        except:
            content = {'Patient does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        try:
            socialdetails = SocialHistory.objects.get(patient=patient)
            return Response(SocialHistorySerializer(socialdetails).data, status=status.HTTP_200_OK)
        except:
            content = {'social details not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, patientid):
        serializer_class = SocialHistorySerializer
        patientid = uuid.UUID(patientid)
        patient = None
        try:
            patient = PatientDetails.objects.get(id=patientid)
        except:
            content = {'Patient does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        
        try:
            socialdetails = SocialHistory.objects.get(patient=patient)
            serializer = SocialHistorySerializer(socialdetails, data=request.data)
            # print(vitaldetails)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            data=request.data
            data['patient']=patientid
            print(data)
            serializer = SocialHistorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class SocialViewSet(ModelViewSet):
#     queryset = SocialHistory.objects.all()
#     serializer_class = SocialHistorySerializer

#     @action(methods=['post'], detail=True)
#     def addsocial(self, request, *args, **kwargs):
#         # target_user = uuid.UUID(kwargs['doctorid'])
#         serializer = SocialHistorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @action(methods=['put'], detail=True)
#     def updatesocial(self, request, *args, **kwargs):
#         social_obj = self.get_object()
#         data = request.data

#         patient = SocialHistory.objects.get(patient=data["patient"])
#         social_obj.patient = patient
#         social_obj.tobacco = data["tobacco"]
#         social_obj.alcohol = data["alcohol"]
#         social_obj.save()

#         serializer = SocialHistorySerializer(social_obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDashboardViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    def get_queryset(self, *args, **kwargs):
        queryset = PatientDetails.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PatientDeshboardSerializer
        elif self.request.method == "PUT":
            return PatientDetailsSerializer

    @action(detail=True, methods=["GET", "PUT"])
    def me(self, request, *args, **kwargs):
        Patient = PatientDetails.objects.get(pk=self.kwargs['pk'])
        if request.method == "GET":
            serializer = PatientDetailsSerializer(Patient)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = PatientDetailsSerializer(Patient, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)