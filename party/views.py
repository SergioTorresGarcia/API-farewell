from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Party, Person
from .serializers import PartySerializer, PersonSerializer


@api_view(['GET'])
def all_data(request, format=None):
    parties = Party.objects.all()
    persons = Person.objects.all()
    serializer1 = PartySerializer(parties, many=True)
    serializer2 = PersonSerializer(persons, many=True)
    return Response({'Party': serializer1.data, 'Person': serializer2.data})


@api_view(['GET', 'POST'])
def party_list(request, format=None):
    if request.method == 'GET':
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def person_list(request, format=None):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id, format=None):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def party_detail(request, id, format=None):
    try:
        party = Party.objects.get(pk=id)
    except Party.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PartySerializer(party)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PartySerializer(party, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

