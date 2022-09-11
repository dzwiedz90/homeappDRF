from django.urls import path

from . import views

app_name = 'humans'
urlpatterns = [
    path('humans/', views.HumanRestApi.as_view()),
    path('humans/<int:id>/', views.ModifyHumanRestApi.as_view()),
    path('treatments/', views.HumanTreatmentRestApi.as_view()),
    path('treatments/<int:id>/', views.ModifyHumanTreatmentRestApi.as_view()),
    path('treatments/updates/', views.HumanTreatmentUpdateRestApi.as_view()),
    path('treatments/updates/<int:id>/', views.ModifyHumanTreatmentUpdateRestApi.as_view()),
    path('diseases/', views.HumanDiseaseRestApi.as_view()),
    path('diseases/<int:id>/', views.ModifyHumanDiseaseRestApi.as_view()),
    path('diseases/updates/', views.HumanDiseaseUpdateRestApi.as_view()),
    path('diseases/updates/<int:id>/', views.ModifyHumanDiseaseUpdateRestApi.as_view()),
    path('tests/', views.HumanMedicalTestRestApi.as_view()),
    path('tests/<int:id>/', views.ModifyHumanMedicalTestRestApi.as_view()),
    path('weight/', views.HumanWeightRestApi.as_view()),
    path('weight/<int:id>/', views.ModifyHumanWeightRestApi.as_view()),
    path('information/', views.HumanGeneralInformationRestApi.as_view()),
    path('information/<int:id>/', views.ModifyHumanGeneralInformationRestApi.as_view()),
]
