from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework import status, generics
from .models import DoctorDetails, PatientDetails
from .serializers import DoctorDetailsSerializer, PatientDetailsSerializer, PatientDeshboardSerializer, \
    DoctorDeshboardSerializer
from .utils import Util


class SearchPatient(APIView):
    def get(self, request, doctorid, search_term):
        doctor = DoctorDetails.objects.get(pk=doctorid)
        patient = PatientDetails.objects.filter(doctor=doctor)
        patient = PatientDetails.objects.filter(doctor=doctor).filter(name__icontains=search_term)
        serializer = DoctorDeshboardSerializer(patient, many=True)
        return Response(serializer.data)


class Details(APIView):

    def get(self, request, doctorid):
        doctor = DoctorDetails.objects.get(pk=doctorid)
        patient = PatientDetails.objects.filter(doctor=doctor)
        serializer = DoctorDeshboardSerializer(patient, many=True)
        return Response(serializer.data)


class PatientViewSet(ModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

    @action(methods=['post'], detail=True)
    def addpatient(self, request, *args, **kwargs):
        serializer = PatientDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user_id = PatientDetails.objects.filter(email_id=user_data['email_id'])
        email_body = 'Hii use the below credential for login' + " " + str(user_id) + " " + 'use only for personal use '
        data = {
            'email_body': email_body,
            'email_subject': 'Login credential'
        }
        Util.sent_email(data, user_data['email_id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
