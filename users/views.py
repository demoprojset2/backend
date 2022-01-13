from django.db.models.fields import UUIDField
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.models import  PatientDetails
import uuid
from backend.serializers import PatientDetailsSerializer
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes


class DoctorViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

        
    @action(methods=['get'], detail=True)
    def me(self, request, *args, **kwargs):
        print(request.user)
        target_user = uuid.UUID(kwargs['doctorid'])
        try:
            doctor = Profile.objects.get(id=target_user)
            serializer = ProfileSerializer(doctor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PatientViewSet(ModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer
    permission_classes = (IsAuthenticated,)


    @action(methods=['post'], detail=True)
    def addpatient(self, request, *args, **kwargs):
        target_user = uuid.UUID(kwargs['doctorid'])
        serializer = PatientDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
     
    