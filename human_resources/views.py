from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Treatment, Disease, MedicalTest, Clinic
from .serializers import GetAllTreatmentsSerializer, CreateTreatmentSerializer, GetAllDiseasesSerializer, \
    CreateDiseaseSerializer, GetAllMedicalTestsSerializer, CreateMedicalTesSerializer, GetAllClinicsSerializer, \
    CreateClinicSerializer, UpdateClinicSerializer, UpdateDiseaseSerializer, UpdateMedicalTestSerializer, \
    UpdateTreatmentSerializer


class TreatmentRestApi(APIView):

    def get(self, request):
        treatments = Treatment.objects.all().filter(is_archived=False)
        serializer = GetAllTreatmentsSerializer(treatments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateTreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Treatment created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add treatment, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyTreatmentRestApi(APIView):

    def put(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
            serializer = UpdateTreatmentSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(treatment, serializer.validated_data)
                return Response({'message': 'Treatment updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update treatment, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Treatment.DoesNotExist:
            return Response({'message': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
            treatment.is_archived = True
            treatment.save()
            return Response({'message': 'Treatment archived'}, status=status.HTTP_200_OK)
        except Treatment.DoesNotExist:
            return Response({'message': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
            treatment.is_archived = False
            treatment.save()
            return Response({'message': 'Treatment restored'}, status=status.HTTP_200_OK)
        except Treatment.DoesNotExist:
            return Response({'message': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)


class DiseaseRestApi(APIView):

    def get(self, request):
        diseases = Disease.objects.all().filter(is_archived=False)
        serializer = GetAllDiseasesSerializer(diseases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateDiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Disease created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add disease, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyDiseaseRestApi(APIView):

    def put(self, request, id):
        try:
            disease = Disease.objects.get(id=id)
            serializer = UpdateDiseaseSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(disease, serializer.validated_data)
                return Response({'message': 'Disease updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update disease, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Disease.DoesNotExist:
            return Response({'message': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            disease = Disease.objects.get(id=id)
            disease.is_archived = True
            disease.save()
            return Response({'message': 'Disease archived'}, status=status.HTTP_200_OK)
        except Disease.DoesNotExist:
            return Response({'message': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            disease = Disease.objects.get(id=id)
            disease.is_archived = False
            disease.save()
            return Response({'message': 'Disease restored'}, status=status.HTTP_200_OK)
        except Disease.DoesNotExist:
            return Response({'message': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)


class MedicalTestRestApi(APIView):

    def get(self, request):
        medical_tests = MedicalTest.objects.all().filter(is_archived=False)
        serializer = GetAllMedicalTestsSerializer(medical_tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateMedicalTesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Medical test created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add medical test, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyMedicalTestRestApi(APIView):

    def put(self, request, id):
        try:
            medical_test = MedicalTest.objects.get(id=id)
            serializer = UpdateMedicalTestSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(medical_test, serializer.validated_data)
                return Response({'message': 'Medical test updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update medical test, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except MedicalTest.DoesNotExist:
            return Response({'message': 'Medical test not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            medical_test = MedicalTest.objects.get(id=id)
            medical_test.is_archived = True
            medical_test.save()
            return Response({'message': 'Medical test archived'}, status=status.HTTP_200_OK)
        except MedicalTest.DoesNotExist:
            return Response({'message': 'Medical test not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            medical_test = MedicalTest.objects.get(id=id)
            medical_test.is_archived = False
            medical_test.save()
            return Response({'message': 'Medical test restored'}, status=status.HTTP_200_OK)
        except MedicalTest.DoesNotExist:
            return Response({'message': 'Medical test not found'}, status=status.HTTP_404_NOT_FOUND)


class ClinicRestApi(APIView):

    def get(self, request):
        clinics = Clinic.objects.all().filter(is_archived=False)
        serializer = GetAllClinicsSerializer(clinics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Clinic created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add clinic, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)


class ModifyClinicRestApi(APIView):

    def put(self, request, id):
        try:
            clinic = Clinic.objects.get(id=id)
            serializer = UpdateClinicSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.update(clinic, serializer.validated_data)
                return Response({'message': 'Clinic updated'}, status=status.HTTP_200_OK)
            return Response({'message': 'Cant update clinic, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Clinic.DoesNotExist:
            return Response({'message': 'Clinic not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            clinic = Clinic.objects.get(id=id)
            clinic.is_archived = True
            clinic.save()
            return Response({'message': 'Clinic archived'}, status=status.HTTP_200_OK)
        except Clinic.DoesNotExist:
            return Response({'message': 'Clinic not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            clinic = Clinic.objects.get(id=id)
            clinic.is_archived = False
            clinic.save()
            return Response({'message': 'Clinic restored'}, status=status.HTTP_200_OK)
        except Clinic.DoesNotExist:
            return Response({'message': 'Clinic not found'}, status=status.HTTP_404_NOT_FOUND)
