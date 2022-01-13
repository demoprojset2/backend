from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('<str:doctorid>/me',views.DoctorViewSet.as_view({"get":"me"})),
    path('<str:doctorid>/addpatient',views.PatientViewSet.as_view({"post":"addpatient"}))
]
