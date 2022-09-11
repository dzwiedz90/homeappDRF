from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Animal
from .serializers import GetAllAnimalsSerializer, CreateAnimalSerializer


class AnimalRestApi(APIView):

    def get(self, request):
        animals = Animal.objects.all()
        serializer = GetAllAnimalsSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateAnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Animal created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add animal, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)
