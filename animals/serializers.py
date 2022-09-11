from rest_framework import serializers

from .models import Animal


class GetAllAnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'animal_name', 'species', 'breed']


class CreateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed']

        def save(self, instance, validated_data):
            instance.animal_name = validated_data.get('animal_name', instance.animal_name)
            instance.species = validated_data.get('species', instance.species)
            instance.breed = validated_data.get('breed', instance.breed)
            instance.save()
            return instance
