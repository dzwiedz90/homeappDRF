from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Human, HumanTreatment, TreatmentUpdate, HumanDisease, DiseaseUpdate, HumanMedicalTests, \
    HumanWeight, HumanGeneralInformation
from .serializers import GetAllHumansSerializer, CreateHumanSerializer, GetAllHumansTreatmentsSerializer, \
    CreateHumanTreatmentSerializer, GetAllHumanTreatmentUpdatesSerializer, CreateHumanTreatmentUpdateSerializer, \
    GetAllHumansDiseasesSerializer, CreateHumanDiseaseSerializer, GetAllHumanDiseaseUpdatesSerializer, \
    CreateHumanDiseaseUpdateSerializer, GetAllHumanMedicalTestsSerializer, CreateHumanMedicalTestSerializer, \
    GetAllHumanWeightSerializer, CreateHumanWeightSerializer, GetAllHumanGeneralInformationsSerializer, \
    CreateHumanGeneralInformationSerializer, UpdateHumanSerializer, UpdateHumanTreatmentSerializer, \
    UpdateHumanDiseaseSerializer, UpdateHumanWeightSerializer, UpdateHumanMedicalTestSerializer, \
    UpdateHumanGeneralInformationSerializer, UpdateHumanDiseaseUpdateSerializer, UpdateHumanTreatmentUpdateSerializer


class HumanRestApi(APIView):

    def get(self, request):
        humans = Human.objects.all().filter(is_archived=False)
        serializer = GetAllHumansSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanRestApi(APIView):

    def put(self, request, id):
        try:
            human = Human.objects.get(id=id)
            serializer = UpdateHumanSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human, serializer.validated_data)
                return Response({'message': 'Human updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human, wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        except Human.DoesNotExist:
            return Response({'message': 'Human not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human = Human.objects.get(id=id)
            human.is_archived = True
            human.save()
            return Response({'message': 'Human archived'}, status=status.HTTP_200_OK)
        except Human.DoesNotExist:
            return Response({'message': 'Human not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human = Human.objects.get(id=id)
            human.is_archived = False
            human.save()
            return Response({'message': 'Human restored'}, status=status.HTTP_200_OK)
        except Human.DoesNotExist:
            return Response({'message': 'Human not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanTreatmentRestApi(APIView):

    def get(self, request):
        human_treatments = HumanTreatment.objects.all().filter(is_archived=False)
        serializer = GetAllHumansTreatmentsSerializer(human_treatments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanTreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human treatment created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human treatment, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanTreatmentRestApi(APIView):

    def put(self, request, id):
        try:
            human_treatment = HumanTreatment.objects.get(id=id)
            serializer = UpdateHumanTreatmentSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_treatment, serializer.validated_data)
                return Response({'message': 'Human treatment updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human treatment, wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        except HumanTreatment.DoesNotExist:
            return Response({'message': 'Human treatment not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_treatment = HumanTreatment.objects.get(id=id)
            human_treatment.is_archived = True
            human_treatment.save()
            return Response({'message': 'Human treatment archived'}, status=status.HTTP_200_OK)
        except HumanTreatment.DoesNotExist:
            return Response({'message': 'Human treatment not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_treatment = HumanTreatment.objects.get(id=id)
            human_treatment.is_archived = False
            human_treatment.save()
            return Response({'message': 'Human treatment restored'}, status=status.HTTP_200_OK)
        except HumanTreatment.DoesNotExist:
            return Response({'message': 'Human treatment not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanTreatmentUpdateRestApi(APIView):

    def get(self, request):
        human_treatment_update = TreatmentUpdate.objects.all().filter(is_archived=False)
        serializer = GetAllHumanTreatmentUpdatesSerializer(human_treatment_update, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanTreatmentUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human treatment update created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human treatment update, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanTreatmentUpdateRestApi(APIView):

    def put(self, request, id):
        try:
            human_treatment_update = TreatmentUpdate.objects.get(id=id)
            serializer = UpdateHumanTreatmentUpdateSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_treatment_update, serializer.validated_data)
                return Response({'message': 'Human treatment update updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human treatment update, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except TreatmentUpdate.DoesNotExist:
            return Response({'message': 'Human treatment update not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_treatment_update = TreatmentUpdate.objects.get(id=id)
            human_treatment_update.is_archived = True
            human_treatment_update.save()
            return Response({'message': 'Human treatment update archived'}, status=status.HTTP_200_OK)
        except TreatmentUpdate.DoesNotExist:
            return Response({'message': 'Human treatment update not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_treatment_update = TreatmentUpdate.objects.get(id=id)
            human_treatment_update.is_archived = False
            human_treatment_update.save()
            return Response({'message': 'Human treatment update restored'}, status=status.HTTP_200_OK)
        except TreatmentUpdate.DoesNotExist:
            return Response({'message': 'Human treatment update not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanDiseaseRestApi(APIView):

    def get(self, request):
        human_diseases = HumanDisease.objects.all().filter(is_archived=False)
        serializer = GetAllHumansDiseasesSerializer(human_diseases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanDiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human disease created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human disease, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanDiseaseRestApi(APIView):

    def put(self, request, id):
        try:
            human_disease = HumanDisease.objects.get(id=id)
            serializer = UpdateHumanDiseaseSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_disease, serializer.validated_data)
                return Response({'message': 'Human disease updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human disease, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except HumanDisease.DoesNotExist:
            return Response({'message': 'Human disease not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_disease = HumanDisease.objects.get(id=id)
            human_disease.is_archived = True
            human_disease.save()
            return Response({'message': 'Human disease archived'}, status=status.HTTP_200_OK)
        except HumanDisease.DoesNotExist:
            return Response({'message': 'Human disease not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_disease = HumanDisease.objects.get(id=id)
            human_disease.is_archived = False
            human_disease.save()
            return Response({'message': 'Human disease restored'}, status=status.HTTP_200_OK)
        except HumanDisease.DoesNotExist:
            return Response({'message': 'Human disease not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanDiseaseUpdateRestApi(APIView):

    def get(self, request):
        human_disease_update = DiseaseUpdate.objects.all().filter(is_archived=False)
        serializer = GetAllHumanDiseaseUpdatesSerializer(human_disease_update, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanDiseaseUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human disease update created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human disease update, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanDiseaseUpdateRestApi(APIView):

    def put(self, request, id):
        try:
            human_disease_update = DiseaseUpdate.objects.get(id=id)
            serializer = UpdateHumanDiseaseUpdateSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_disease_update, serializer.validated_data)
                return Response({'message': 'Human disease update updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human disease update, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except DiseaseUpdate.DoesNotExist:
            return Response({'message': 'Human disease update not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_disease_update = DiseaseUpdate.objects.get(id=id)
            human_disease_update.is_archived = True
            human_disease_update.save()
            return Response({'message': 'Human disease update archived'}, status=status.HTTP_200_OK)
        except DiseaseUpdate.DoesNotExist:
            return Response({'message': 'Human disease update not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_disease_update = DiseaseUpdate.objects.get(id=id)
            human_disease_update.is_archived = False
            human_disease_update.save()
            return Response({'message': 'Human disease update restored'}, status=status.HTTP_200_OK)
        except DiseaseUpdate.DoesNotExist:
            return Response({'message': 'Human disease update not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanMedicalTestRestApi(APIView):

    def get(self, request):
        human_medical_tests = HumanMedicalTests.objects.all().filter(is_archived=False)
        serializer = GetAllHumanMedicalTestsSerializer(human_medical_tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanMedicalTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human medical test created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human medical test, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanMedicalTestRestApi(APIView):

    def put(self, request, id):
        try:
            human_medical_tests = HumanMedicalTests.objects.get(id=id)
            if 'file' in request.POST:
                human_medical_tests.file = request.POST['file']
                human_medical_tests.save()
            serializer = UpdateHumanMedicalTestSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_medical_tests, serializer.validated_data)
                return Response({'message': 'Human medical test updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human medical test, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except HumanMedicalTests.DoesNotExist:
            return Response({'message': 'Human medical test not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_medical_tests = HumanMedicalTests.objects.get(id=id)
            human_medical_tests.is_archived = True
            human_medical_tests.save()
            return Response({'message': 'Human medical test archived'}, status=status.HTTP_200_OK)
        except HumanMedicalTests.DoesNotExist:
            return Response({'message': 'Human medical test not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_medical_tests = HumanMedicalTests.objects.get(id=id)
            human_medical_tests.is_archived = False
            human_medical_tests.save()
            return Response({'message': 'Human medical test restored'}, status=status.HTTP_200_OK)
        except HumanMedicalTests.DoesNotExist:
            return Response({'message': 'Human medical test not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanWeightRestApi(APIView):

    def get(self, request):
        human_weight = HumanWeight.objects.all().filter(is_archived=False)
        serializer = GetAllHumanWeightSerializer(human_weight, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanWeightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            human = Human.objects.get(id=request.data['human'])
            human.current_weight = request.data['weight']
            human.save()
            return Response({'message': 'Human weight created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human weight, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanWeightRestApi(APIView):

    def put(self, request, id):
        try:
            human_weight = HumanWeight.objects.get(id=id)
            serializer = UpdateHumanWeightSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_weight, serializer.validated_data)
                return Response({'message': 'Human weight updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human weight, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except HumanWeight.DoesNotExist:
            return Response({'message': 'Human weight not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_weight = HumanWeight.objects.get(id=id)
            human_weight.is_archived = True
            human_weight.save()
            return Response({'message': 'Human weight archived'}, status=status.HTTP_200_OK)
        except HumanWeight.DoesNotExist:
            return Response({'message': 'Human weight not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_weight = HumanWeight.objects.get(id=id)
            human_weight.is_archived = False
            human_weight.save()
            return Response({'message': 'Human weight restored'}, status=status.HTTP_200_OK)
        except HumanWeight.DoesNotExist:
            return Response({'message': 'Human weight not found'}, status=status.HTTP_404_NOT_FOUND)


class HumanGeneralInformationRestApi(APIView):

    def get(self, request):
        human_general_information = HumanGeneralInformation.objects.all().filter(is_archived=False)
        serializer = GetAllHumanGeneralInformationsSerializer(human_general_information, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateHumanGeneralInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Human general information created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add human general information, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyHumanGeneralInformationRestApi(APIView):

    def put(self, request, id):
        try:
            human_general_information = HumanGeneralInformation.objects.get(id=id)
            serializer = UpdateHumanGeneralInformationSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(human_general_information, serializer.validated_data)
                return Response({'message': 'Human general information updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update human general information, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except HumanGeneralInformation.DoesNotExist:
            return Response({'message': 'Human general information not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            human_general_information = HumanGeneralInformation.objects.get(id=id)
            human_general_information.is_archived = True
            human_general_information.save()
            return Response({'message': 'Human general information archived'}, status=status.HTTP_200_OK)
        except HumanGeneralInformation.DoesNotExist:
            return Response({'message': 'Human general information not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            human_general_information = HumanGeneralInformation.objects.get(id=id)
            human_general_information.is_archived = False
            human_general_information.save()
            return Response({'message': 'Human general information restored'}, status=status.HTTP_200_OK)
        except HumanGeneralInformation.DoesNotExist:
            return Response({'message': 'Human general information not found'}, status=status.HTTP_404_NOT_FOUND)
