import os

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import generic

from human_resources.models import Treatment, Disease, MedicalTest, Clinic
from humans.models import Human, HumanTreatment, HumanDisease, HumanMedicalTests, HumanWeight, HumanGeneralInformation, \
    TreatmentUpdate, DiseaseUpdate
from .forms import HumanForm, HumanTreatmentForm, CreateHumanTreatmentForm, HumanDiseaseForm, CreateHumanDiseaseForm, \
    HumanMedicalTestForm, CreateHumanMedicalTestForm, HumanWeightForm, HumanInformationtForm, TreatmentForm, \
    DiseaseForm, TestForm, ClinicForm, TreatmentUpdateForm, DiseaseUpdateForm


class IndexView(generic.ListView):
    template_name = 'humans_ui/index.html'
    context_object_name = 'humans_list'

    def get_queryset(self):
        return Human.objects.all()


def get_human(request, pk):
    if request.method == 'GET':
        human = Human.objects.all().filter(id=pk)
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_details.html',
                                {'human': human, 'pk': pk})


def create_human(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'gender': request.POST['gender'], 'date_born': request.POST['date_born'],
                'height': request.POST['height'], 'current_weight': request.POST['current_weight']}
        url = 'http://localhost:8000/api/humans/humans/'

        last_human = Human.objects.all().last()
        if last_human:
            pk = last_human.id + 1
        else:
            pk = 1
        photo = request.FILES['file']
        path = default_storage.save(str(pk) + os.sep + 'photos' + os.sep + photo.name, ContentFile(photo.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        data['photo'] = tmp_file.split('media')[1]

        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        return render(request, 'humans_ui/create/add_human.html')


def update_human(request, pk):
    if request.method == 'POST':
        data = {'name': request.POST['human_name'], 'gender': request.POST['gender'],
                'date_born': request.POST['date_born'], 'height': request.POST['height'],
                'current_weight': request.POST['current_weight']}

        photo = request.FILES['file']
        path = default_storage.save(str(pk) + os.sep + 'photos' + os.sep + photo.name, ContentFile(photo.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        data['photo'] = tmp_file.split('media')[1]

        if 'is_archived' in request.POST:
            data['is_archived']: request.POST['is_archived']
        url = 'http://localhost:8000/api/humans/humans/' + str(pk) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanForm()
        human = Human.objects.get(pk=pk)
    return render(request, 'humans_ui/modify/modify_human.html', {'form': form, 'pk': pk, 'human': human})


def get_human_treatment(request, pk):
    if request.method == 'GET':
        human_treatment_list = HumanTreatment.objects.all().filter(human=pk)
        treatment_updates_list = []
        try:
            for treatment in human_treatment_list:
                item = TreatmentUpdate.objects.all().filter(human_treatment=treatment.id)
                if item:
                    treatment_updates_list.append(item)
        except TreatmentUpdate.DoesNotExist:
            pass
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_treatment_details.html',
                                {'human_treatment_list': human_treatment_list, 'pk': pk,
                                 'treatment_updates_list': treatment_updates_list})


def create_human_treatment(request, pk):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'treatment': request.POST['treatment'],
                'clinic': request.POST['clinic'], 'date_occurred': request.POST['date_occurred'],
                'description': request.POST['description'], 'satisfaction': request.POST['satisfaction'],
                'doctor': request.POST['doctor']}
        url = 'http://localhost:8000/api/humans/treatments/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = CreateHumanTreatmentForm()
        treatments = Treatment.objects.all()
        return render(request, 'humans_ui/create/add_human_treatment.html',
                      {'form': form, 'pk': pk, 'treatments': treatments})


def update_human_treatment(request, pk, id):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'treatment': request.POST['treatment'],
                'clinic': request.POST['clinic'], 'date_occurred': request.POST['date_occurred'],
                'date_treated': request.POST['date_treated'], 'description': request.POST['description'],
                'satisfaction': request.POST['satisfaction'], 'doctor': request.POST['doctor']}
        url = 'http://localhost:8000/api/humans/treatments/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanTreatmentForm()
        treatment = HumanTreatment.objects.get(id=id)
        treatments = Treatment.objects.all()
    return render(request, 'humans_ui/modify/modify_human_treatment.html',
                  {'form': form, 'pk': pk, 'id': id, 'treatment': treatment, 'treatments': treatments})


def create_treatment_update(request, pk, id):
    if request.method == 'POST':
        data = {'treatment_update': request.POST['treatment_update'], 'human_treatment': id}
        url = 'http://localhost:8000/api/humans/treatments/updates/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentUpdateForm()
        return render(request, 'humans_ui/create/add_treatment_update.html',
                      {'form': form, 'pk': pk, 'id': id})


def update_treatment_update(request, pk, id, upid):
    if request.method == 'POST':
        data = {'treatment_update': request.POST['treatment_update'], 'human_treatment': id}
        url = 'http://localhost:8000/api/humans/treatments/updates/' + str(upid) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentUpdateForm()
        treatment_update = TreatmentUpdate.objects.get(id=upid)
    return render(request, 'humans_ui/modify/modify_treatment_update.html',
                  {'form': form, 'pk': pk, 'id': id, 'treatment_update': treatment_update, 'upid': upid})


def get_human_diseases(request, pk):
    if request.method == 'GET':
        human_disease_list = HumanDisease.objects.all().filter(human=pk)
        disease_updates_list = []
        try:
            for disease in human_disease_list:
                item = DiseaseUpdate.objects.all().filter(human_disease=disease.id)
                if item:
                    disease_updates_list.append(item)
        except TreatmentUpdate.DoesNotExist:
            pass
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_disease_details.html',
                                {'human_disease_list': human_disease_list, 'pk': pk,
                                 'disease_updates_list': disease_updates_list})


def create_human_disease(request, pk):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'disease': request.POST['disease'],
                'clinic': request.POST['clinic'], 'date_occurred': request.POST['date_occurred'],
                'description': request.POST['description'], 'satisfaction': request.POST['satisfaction'],
                'doctor': request.POST['doctor']}
        url = 'http://localhost:8000/api/humans/diseases/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = CreateHumanDiseaseForm()
        return render(request, 'humans_ui/create/add_human_disease.html', {'form': form, 'pk': pk})


def update_human_disease(request, pk, id):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'disease': request.POST['disease'],
                'clinic': request.POST['clinic'], 'date_occurred': request.POST['date_occurred'],
                'date_treated': request.POST['date_treated'], 'description': request.POST['description'],
                'satisfaction': request.POST['satisfaction'], 'doctor': request.POST['doctor']}
        url = 'http://localhost:8000/api/humans/diseases/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanDiseaseForm()
        disease = HumanDisease.objects.get(id=id)
        diseases = Disease.objects.all()
    return render(request, 'humans_ui/modify/modify_human_disease.html',
                  {'form': form, 'pk': pk, 'id': id, 'disease': disease, 'diseases': diseases})


def create_disease_update(request, pk, id):
    if request.method == 'POST':
        data = {'disease_update': request.POST['disease_update'],
                'human_disease': id}
        url = 'http://localhost:8000/api/humans/diseases/updates/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DiseaseUpdateForm()
        return render(request, 'humans_ui/create/add_disease_update.html',
                      {'form': form, 'pk': pk, 'id': id})


def update_disease_update(request, pk, id, upid):
    if request.method == 'POST':
        data = {'disease_update': request.POST['disease_update'], 'human_disease': id}
        url = 'http://localhost:8000/api/humans/diseases/updates/' + str(upid) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DiseaseUpdateForm()
        disease_update = DiseaseUpdate.objects.get(id=upid)
    return render(request, 'humans_ui/modify/modify_disease_update.html',
                  {'form': form, 'pk': pk, 'id': id, 'disease_update': disease_update, 'upid': upid})


def get_human_medical_tests(request, pk):
    if request.method == 'GET':
        human_medical_test_list = HumanMedicalTests.objects.all().filter(human=pk)
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_medical_test_details.html',
                                {'human_medical_test_list': human_medical_test_list, 'pk': pk})


def create_human_test(request, pk):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'medical_test': request.POST['medical_test'],
                'date_taken': request.POST['date_taken'], 'clinic': request.POST['clinic'],
                'ordering_unit': request.POST['ordering_unit'],
                'satisfaction': request.POST['satisfaction'], 'description': request.POST['description'],
                'results': request.POST['results']}
        url = 'http://localhost:8000/api/humans/tests/'

        file = request.FILES['file']
        path = default_storage.save(str(pk) + os.sep + 'tests' + os.sep + file.name, ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        data['file'] = tmp_file

        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/tests/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = CreateHumanMedicalTestForm()
        return render(request, 'humans_ui/create/add_human_medical_test.html', {'form': form, 'pk': pk})


def update_human_test(request, pk, id):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'medical_test': request.POST['medical_test'],
                'date_taken': request.POST['date_taken'],
                'clinic': request.POST['clinic'], 'ordering_unit': request.POST['ordering_unit'],
                'description': request.POST['description'],
                'satisfaction': request.POST['satisfaction'], 'results': request.POST['results']}
        url = 'http://localhost:8000/api/humans/tests/' + str(id) + '/'

        file = request.FILES['file']
        path = default_storage.save(str(pk) + os.sep + 'tests' + os.sep + file.name, ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        data['file'] = tmp_file

        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/tests/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanMedicalTestForm()
        test = HumanMedicalTests.objects.get(id=id)
    return render(request, 'humans_ui/modify/modify_human_medical_test.html',
                  {'form': form, 'pk': pk, 'id': id, 'test': test})


def get_human_weight(request, pk):
    if request.method == 'GET':
        human_weight_list = HumanWeight.objects.all().filter(human=pk)
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_weight_details.html',
                                {'human_weight_list': human_weight_list, 'pk': pk})


def create_human_weight(request, pk):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'date_of_measurement': request.POST['date_of_measurement'],
                'weight': request.POST['weight']}
        url = 'http://localhost:8000/api/humans/weight/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/weight/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanWeightForm()
        return render(request, 'humans_ui/create/add_human_weight.html', {'form': form, 'pk': pk})


def update_human_weight(request, pk, id):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'date_of_measurement': request.POST['date_of_measurement'],
                'weight': request.POST['weight']}
        url = 'http://localhost:8000/api/humans/weight/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/weight/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanWeightForm()
        weight = HumanWeight.objects.get(id=id)
    return render(request, 'humans_ui/modify/modify_human_weight.html',
                  {'form': form, 'pk': pk, 'id': id, 'weight': weight})


def get_human_general_information(request, pk):
    if request.method == 'GET':
        human_general_information_list = HumanGeneralInformation.objects.all().filter(human=pk)
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_general_information_details.html',
                                {'human_general_information_list': human_general_information_list, 'pk': pk})


def create_human_information(request, pk):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'content': request.POST['content']}
        url = 'http://localhost:8000/api/humans/information/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/information/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanInformationtForm()
        return render(request, 'humans_ui/create/add_human_information.html', {'form': form, 'pk': pk})


def update_human_information(request, pk, id):
    if request.method == 'POST':
        data = {'human': request.POST['human'], 'content': request.POST['content']}
        url = 'http://localhost:8000/api/humans/information/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/' + str(pk) + '/human/information/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = HumanInformationtForm()
        information = HumanGeneralInformation.objects.get(id=id)
    return render(request, 'humans_ui/modify/modify_human_information.html',
                  {'form': form, 'pk': pk, 'id': id, 'information': information})


def get_treatments(request):
    if request.method == 'GET':
        treatments_list = Treatment.objects.all()
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_resources' + os.sep + 'treatment.html',
                                {'treatments_list': treatments_list})


def create_treatment(request):
    if request.method == 'POST':
        data = {'treatment_name': request.POST['treatment_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/treatments/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/resources/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        return render(request, 'humans_ui/human_resources/create/add_treatment.html', {'form': form})


def update_treatment(request, id):
    if request.method == 'POST':
        data = {'treatment_name': request.POST['treatment_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/treatments/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/resources/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        treatment = Treatment.objects.get(id=id)
    return render(request, 'humans_ui/human_resources/modify/modify_treatment.html',
                  {'form': form, 'id': id, 'treatment': treatment})


def get_disease(request):
    if request.method == 'GET':
        diseases_list = Disease.objects.all()
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_resources' + os.sep + 'diseases.html',
                                {'diseases_list': diseases_list})


def create_disease(request):
    if request.method == 'POST':
        data = {'disease_name': request.POST['disease_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/diseases/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/resources/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DiseaseForm()
        return render(request, 'humans_ui/human_resources/create/add_disease.html', {'form': form})


def update_disease(request, id):
    if request.method == 'POST':
        data = {'disease_name': request.POST['disease_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/diseases/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/resources/diseases/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DiseaseForm()
        disease = Disease.objects.get(id=id)
    return render(request, 'humans_ui/human_resources/modify/modify_disease.html',
                  {'form': form, 'id': id, 'disease': disease})


def get_test(request):
    if request.method == 'GET':
        tests_list = MedicalTest.objects.all()
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_resources' + os.sep + 'tests.html',
                                {'tests_list': tests_list})


def create_test(request):
    if request.method == 'POST':
        data = {'medical_test_name': request.POST['medical_test_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/tests/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/resources/tests/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        return render(request, 'humans_ui/human_resources/create/add_test.html', {'form': form})


def update_test(request, id):
    if request.method == 'POST':
        data = {'medical_test_name': request.POST['medical_test_name'], 'description': request.POST['description']}
        url = 'http://localhost:8000/api/humans/resources/tests/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/resources/tests/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        test = MedicalTest.objects.get(id=id)
    return render(request, 'humans_ui/human_resources/modify/modify_test.html',
                  {'form': form, 'id': id, 'test': test})


def get_clinic(request):
    if request.method == 'GET':
        clinics_list = Clinic.objects.all()
        return TemplateResponse(request, 'humans_ui' + os.sep + 'human_resources' + os.sep + 'clinics.html',
                                {'clinics_list': clinics_list})


def create_clinic(request):
    if request.method == 'POST':
        data = {'clinic_name': request.POST['clinic_name'], 'address': request.POST['address'],
                'phone_number': request.POST['phone_number'], 'opening_hours': request.POST['opening_hours']}
        url = 'http://localhost:8000/api/humans/resources/clinics/'
        request = requests.post(url, data=data)
        if request.status_code == 201:
            return HttpResponseRedirect('/ui/humans/resources/clinics/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        return render(request, 'humans_ui/human_resources/create/add_clinic.html', {'form': form})


def update_clinic(request, id):
    if request.method == 'POST':
        data = {'clinic_name': request.POST['clinic_name'], 'address': request.POST['address'],
                'phone_number': request.POST['phone_number'], 'opening_hours': request.POST['opening_hours']}
        url = 'http://localhost:8000/api/humans/resources/clinics/' + str(id) + '/'
        request = requests.put(url, data=data)
        if request.status_code == 200:
            return HttpResponseRedirect('/ui/humans/resources/clinics/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentForm()
        clinic = Clinic.objects.get(id=id)
    return render(request, 'humans_ui/human_resources/modify/modify_clinic.html',
                  {'form': form, 'id': id, 'clinic': clinic})


def view_file(request, pk):
    image_data = open(request.POST['path'], "rb").read()
    type = request.POST['path'].split('.')[1]
    if type == 'jpg':
        content_type = 'image/jpg'
    elif type == 'png':
        content_type = 'image/png'
    elif type == 'pdf':
        content_type = 'application/pdf'
    return HttpResponse(image_data, content_type=content_type)


def report(request):
    if request.method == 'POST':
        if request.POST:
            data_to_print = []
            data = dict(request.POST)
            del data['csrfmiddlewaretoken']
            del data['pk']
            for item in data:
                if 'treatment' in item:
                    a = data[item][0]
                    data_to_print.append(HumanTreatment.objects.get(id=int(data[item][0])))
                elif 'disease' in item:
                    data_to_print.append(HumanDisease.objects.get(id=int(data[item][0])))
                elif 'information' in item:
                    data_to_print.append(HumanGeneralInformation.objects.get(id=int(data[item][0])))
            human = Human.objects.get(id=request.POST['pk'])

            human_treatment_list = HumanTreatment.objects.all().filter(human=request.POST['pk'])
            treatment_updates_list = []
            try:
                for treatment in human_treatment_list:
                    item = TreatmentUpdate.objects.all().filter(human_treatment=treatment.id)
                    if item:
                        treatment_updates_list.append(item)
            except TreatmentUpdate.DoesNotExist:
                pass

            human_disease_list = HumanDisease.objects.all().filter(human=request.POST['pk'])
            disease_updates_list = []
            try:
                for disease in human_disease_list:
                    item = DiseaseUpdate.objects.all().filter(human_disease=disease.id)
                    if item:
                        disease_updates_list.append(item)
            except TreatmentUpdate.DoesNotExist:
                pass

            return render(request, 'humans_ui/generated_report.html',
                          {'data': data_to_print, 'human': human, 'treatment_updates_list': treatment_updates_list,
                           'disease_updates_list': disease_updates_list})
    else:
        treatments = HumanTreatment.objects.all().filter(human=request.GET['pk'])
        diseases = HumanDisease.objects.all().filter(human=request.GET['pk'])
        informations = HumanGeneralInformation.objects.all().filter(human=request.GET['pk'])
        return render(request, 'humans_ui/report.html',
                      {'pk': request.GET['pk'], 'treatments': treatments, 'diseases': diseases,
                       'informations': informations})
