from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('patient', views.PatientDashboardViewSet, basename='patients')
print(router.urls)
urlpatterns = [
    path('api/doctors/<str:doctorid>/me', views.DoctorViewSet.as_view()),
    path('api/doctors/<str:doctorid>/addpatient', views.PatientViewSet.as_view({"post": "addpatient"})),
    path('', include(router.urls))
]
