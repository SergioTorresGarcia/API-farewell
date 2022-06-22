from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .forms import PersonModelForm, PartyModelForm
from .models import Party, Person
from .serializers import PartySerializer, PersonSerializer


@api_view(['GET']) #API - ALL
def api_all_data(request, format=None):
    parties = Party.objects.all()
    persons = Person.objects.all()
    serializer1 = PartySerializer(parties, many=True)
    serializer2 = PersonSerializer(persons, many=True)
    return Response({'Party': serializer1.data, 'Person': serializer2.data})


@api_view(['GET', 'POST']) #API - PARTY
def api_party_list(request, format=None):
    if request.method == 'GET':
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE']) #API - PARTY-DETAILS
def api_party_detail(request, id, format=None):
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


@api_view(['GET', 'POST']) #API - PERSON
def api_person_list(request, format=None):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE']) #API - PERSON-DETAILS
def api_person_detail(request, id, format=None):
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

#                                                      API ^
############################################################
#                                                   VIEWS v

 #VIEW - HOME
def homepage(request):
    parties = Party.objects.all()
    persons = Person.objects.all().order_by('surname')

    this_sur = Person.id


    inv_people_kids = 0
    inv_people_fri = 0
    inv_people_fam = 0
    inv_people_rest = 0
    sum_kids = 0
    sum_fri = 0
    sum_fam = 0
    sum_rest = 0

    # conf_people = 0
    for person in persons:
        if person.party.name == 'Just Kids':
            inv_people_kids += 1
            if person.confirmed == True:
                sum_kids += 1
        elif person.party.name == 'All Friends':
            inv_people_fri += 1
            if person.confirmed == True:
                sum_fri += 1
        elif person.party.name == 'Family':
            inv_people_fam += 1
            if person.confirmed == True:
                sum_fam += 1
        elif person.party.name == 'Other':
            inv_people_rest += 1
            if person.confirmed == True:
                sum_rest += 1
    return render(request, 'party/farewell.html', {'parties': parties,
                                                   'persons': persons,
                                                   'inv_people_kids': inv_people_kids,
                                                   'inv_people_fri': inv_people_fri,
                                                   'inv_people_fam': inv_people_fam,
                                                   'inv_people_rest': inv_people_rest,
                                                   'sum_kids': sum_kids,
                                                   'sum_fri': sum_fri,
                                                   'sum_fam': sum_fam,
                                                   'sum_rest': sum_rest,
                                                   'this_sur': this_sur
                                                   })
    # for party in parties:
    #     for person in persons:
    #         if person.invited == True:
    #             inv_people += 1
    #         if person.confirmed == True:
    #             conf_people += 1
    #
    # return render(request, 'party/farewell.html', {
    #     'persons': persons,
    #     'parties': parties,
    #     'inv_people': inv_people,
    #     'conf_people': conf_people
    #     })


 # VIEW - PARTY ADD
class AddPartyView(View):
    """ Opens form to add a person """
    def get(self, request):
        form = PartyModelForm()
        return render(request, 'party/form.html', {'form': form})

    def post(self, request):
        form = PartyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'party/form.html', {'form': form})


 #VIEW - PARTY LIST
def party_list(request):
    parties = Party.objects.all()
    return render(request, 'party/farewell.html', {'parties': parties})


 #VIEW - PARTY DETAILS
def party_detail(request, id):
    party = Party.objects.get(pk=id)
    persons = Person.objects.all().order_by('surname')
    inv_people_kids = 0
    inv_people_fri = 0
    inv_people_fam = 0
    inv_people_rest = 0
    for person in persons:
        if person.party.name == 'Just Kids':
            inv_people_kids += 1
        elif person.party.name == 'All Friends':
            inv_people_fri += 1
        elif person.party.name == 'Family':
            inv_people_fam += 1
        elif person.party.name == 'Other':
            inv_people_rest += 1
    return render(request, 'party/detail.html', {   'party':party,
                                                    'persons': persons,
                                                    'inv_people_kids': inv_people_kids,
                                                    'inv_people_fri': inv_people_fri,
                                                    'inv_people_fam': inv_people_fam,
                                                    'inv_people_rest': inv_people_rest
                                                    })

 #VIEW - PARTY EDIT
class EditPartyView(View):
    """ On click, filled form opens allowing to edit data of a particular item from the list """
    def get(self, request, party_id):
        party = Party.objects.get(pk=party_id)
        form = PartyModelForm(instance=party)
        return render(request, 'party/form.html', {'form': form})

    def post(self, request, party_id):
        party = Party.objects.get(pk=party_id)
        form = PartyModelForm(request.POST, request.FILES, instance=party)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'party/form.html', {'form': form})


 # VIEW - PARTY DELETE
class DeletePartyView(View):
    """ On click, button deletes book from the collection """
    def get(self, request, party_id):
        party = Party.objects.get(pk=party_id)
        party.delete()
        return redirect('/')


### PARTY ^     /     v PERSON


 # VIEW - PERSON ADD
class AddPersonView(View):
    """ Opens form to add a person """
    def get(self, request):
        form = PersonModelForm()
        return render(request, 'party/form.html', {'form': form})

    def post(self, request):
        form = PersonModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'party/form.html', {'form': form})


 #VIEW - PERSON LIST
def person_list(request):
    party_names = Party.objects.all()
    persons = Person.objects.all()
    return render(request, 'party/farewell.html', {'persons': persons, 'party_names': party_names})


 #VIEW - PERSON DETAILS
def person_detail(request, id):
    data = Person.objects.get(pk=id)
    return render(request, 'party/detail.html', {'person':data})


 #VIEW - PERSON EDIT
class EditPersonView(View):
    """ On click, filled form opens allowing to edit data of a particular item from the list """
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonModelForm(instance=person)
        return render(request, 'party/form.html', {'form': form})

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonModelForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'party/form.html', {'form': form})


 # VIEW - PERSON DELETE
class DeletePersonView(View):
    """ On click, button deletes book from the collection """
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        person.delete()
        return redirect('/')
