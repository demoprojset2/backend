from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint
router = DefaultRouter()
router.register('patient', views.PatientDashboardViewSet, basename='patients')
urlpatterns = [
   path('api/doctors/<str:doctorid>/search/<str:search_term>', views.SearchPatient.as_view()),
    path('api/doctors/<str:doctorid>', views.Details.as_view()),
    # path('api/doctors/<str:doctorid>/me', views.me),
    path('', include(router.urls)),
    path('api/doctors/<str:doctorid>/addpatient', views.PatientViewSet.as_view({"post": "addpatient"})),
]
