from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls.conf import path, include

router = DefaultRouter()
router.register('patient', views.PatientDashboardViewSet, basename='patients')

urlpatterns = [
    path('api/doctors/<str:doctorid>/me',views.DoctorViewSet.as_view({"get":"me"})),
    path('api/doctors/<str:doctorid>/addpatient',views.PatientAddViewSet.as_view({"post":"addpatient"})),
    path('api/doctors/<str:doctorid>/<str:patientid>/basicdetails',views.PatientViewSet.as_view()),
    path('api/doctors/<str:doctorid>/<str:patientid>/addvitals',views.VitalsViewSet.as_view({"post":"addvitals"})),
    path('api/doctors/<str:doctorid>/<str:patientid>/meds',views.MedicationViewSet.as_view({"get":"meds","post":"meds"})),
    path('api/doctors/<str:patientid>/socialhistory',views.SocialViewSet.as_view()),
    path('', include(router.urls))
]
