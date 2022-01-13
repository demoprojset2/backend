from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls.conf import path, include

router = DefaultRouter()
router.register('patient', views.PatientDashboardViewSet, basename='patients')

urlpatterns = [
    path('api/doctors/<str:doctorid>/me',views.DoctorViewSet.as_view({"get":"me"})),
    path('api/doctors/<str:doctorid>/addpatient',views.PatientViewSet.as_view({"post":"addpatient"})),
    path('api/doctors/<str:doctorid>/<str:patientid>/addvitals',views.VitalsViewSet.as_view({"post":"addvitals"})),
    path('api/doctors/<str:doctorid>/<str:patientid>/addmeds',views.MedicationViewSet.as_view({"post":"addmeds"})),
    path('api/doctors/<str:patientid>/addsocial',views.SocialViewSet.as_view({"post":"addsocial","put":"addsocial"})),
    path('', include(router.urls))
]
