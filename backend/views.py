from django.db.models.fields import UUIDField
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
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


class PatientViewSet(ModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

    @action(methods=['post'], detail=True)
    def addpatient(self, request, *args, **kwargs):
        target_user = uuid.UUID(kwargs['doctorid'])
        serializer = PatientDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

    @action(methods=['post'], detail=True)
    def addmeds(self, request, *args, **kwargs):
        target_user = uuid.UUID(kwargs['doctorid'])
        target_user1 = uuid.UUID(kwargs['patientid'])
        # request.data.
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SocialViewSet(ModelViewSet):
    queryset = SocialHistory.objects.all()
    serializer_class = SocialHistorySerializer

    @action(methods=['get','post','put'], detail=True)
    def addsocial(self, request, *args, **kwargs):
        # target_user = uuid.UUID(kwargs['doctorid'])
        serializer = SocialHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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