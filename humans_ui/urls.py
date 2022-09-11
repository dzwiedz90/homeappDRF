from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

# path('ui/humans/', include('humans_ui.urls')),

app_name = 'humans_ui'
urlpatterns = [
    # GET
    path('', views.IndexView.as_view()),
    path('<int:pk>/human/', views.get_human, name='human_detail'),
    path('<int:pk>/human/treatments/', views.get_human_treatment, name='treatment_detail'),
    path('<int:pk>/human/diseases/', views.get_human_diseases, name='disease_detail'),
    path('<int:pk>/human/tests/', views.get_human_medical_tests, name='medical_test_detail'),
    path('<int:pk>/human/weight/', views.get_human_weight, name='weight_detail'),
    path('<int:pk>/human/information/', views.get_human_general_information, name='general_information_detail'),

    # CREATE
    path('human/add/', views.create_human, name='add_human'),
    path('<int:pk>/human/treatments/add/', views.create_human_treatment, name='add_human_treatment'),
    path('<int:pk>/human/diseases/add/', views.create_human_disease, name='add_human_disease'),
    path('<int:pk>/human/tests/add/', views.create_human_test, name='add_human_test'),
    path('<int:pk>/human/weight/add/', views.create_human_weight, name='update_human_weight'),
    path('<int:pk>/human/information/add/', views.create_human_information, name='create_human_information'),
    path('<int:pk>/human/treatments/add/update/<int:id>/', views.create_treatment_update, name='create_treatment_update'),
    path('<int:pk>/human/diseases/add/update/<int:id>/', views.create_disease_update, name='create_disease_update'),

    # MODIFY
    path('<int:pk>/human/modify/', views.update_human, name='update_human'),
    path('<int:pk>/human/treatments/modify/<int:id>/', views.update_human_treatment, name='update_human_treatment'),
    path('<int:pk>/human/diseases/modify/<int:id>/', views.update_human_disease, name='update_human_disease'),
    path('<int:pk>/human/tests/modify/<int:id>/', views.update_human_test, name='update_human_test'),
    path('<int:pk>/human/weight/modify/<int:id>/', views.update_human_weight, name='update_human_weight'),
    path('<int:pk>/human/information/modify/<int:id>/', views.update_human_information, name='update_human_information'),
    path('<int:pk>/human/treatments/modify/update/<int:id>/<int:upid>/', views.update_treatment_update, name='update_treatment_update'),
    path('<int:pk>/human/diseases/modify/update/<int:id>/<int:upid>/', views.update_disease_update, name='update_disease_update'),

    # HUMAN RESOURCES

    # GET
    path('resources/treatments/', views.get_treatments, name='treatments_details'),
    path('resources/diseases/', views.get_disease, name='diseases_details'),
    path('resources/tests/', views.get_test, name='tests_details'),
    path('resources/clinics/', views.get_clinic, name='clinics_details'),

    # CREATE
    path('resources/treatments/add/', views.create_treatment, name='add_treatment'),
    path('resources/diseases/add/', views.create_disease, name='add_disease'),
    path('resources/tests/add/', views.create_test, name='add_test'),
    path('resources/clinics/add/', views.create_clinic, name='add_clinic'),

    # MODIFY
    path('resources/treatments/modify/<int:id>/', views.update_treatment, name='update_treatment'),
    path('resources/diseases/modify/<int:id>/', views.update_disease, name='update_disease'),
    path('resources/tests/modify/<int:id>/', views.update_test, name='update_test'),
    path('resources/clinics/modify/<int:id>/', views.update_clinic, name='update_clinic'),

    path('<int:pk>/human/tests/file/', views.view_file, name='view_file'),
    path('report/', views.report, name='report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

