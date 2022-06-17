from rest_framework import serializers

from party.models import Party, Person


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['id', 'name', 'when', 'where', 'description']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'invited', 'confirmed', 'party']
