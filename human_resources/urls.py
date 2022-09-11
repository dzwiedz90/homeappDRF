from django.urls import path

from . import views

app_name = 'human_resources'
urlpatterns = [
    path('treatments/', views.TreatmentRestApi.as_view()),
    path('treatments/<int:id>/', views.ModifyTreatmentRestApi.as_view()),
    path('diseases/', views.DiseaseRestApi.as_view()),
    path('diseases/<int:id>/', views.ModifyDiseaseRestApi.as_view()),
    path('tests/', views.MedicalTestRestApi.as_view()),
    path('tests/<int:id>/', views.ModifyMedicalTestRestApi.as_view()),
    path('clinics/', views.ClinicRestApi.as_view()),
    path('clinics/<int:id>/', views.ModifyClinicRestApi.as_view()),
]
