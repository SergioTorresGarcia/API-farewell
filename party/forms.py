from django import forms

from party.models import Person, Party


class PersonModelForm(forms.ModelForm):
    """ Form that allows to add (or modify) a person to the list """
    class Meta:
        model = Person
        labels = {
            'name': '',
            'surname': '',
            'note': ''
        }
        fields = ['name', 'surname', 'invited', 'confirmed', 'party', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'surname'}),
            'invited': forms.CheckboxInput(),
            'confirmed': forms.CheckboxInput(),
            'party': forms.RadioSelect(),
            'note': forms.TextInput(attrs={'placeholder': 'different date?'})
        }


class PartyModelForm(forms.ModelForm):
    """ Form that allows to add (or modify) a person to the list """
    class Meta:
        model = Party
        labels={
            'name':'',
            'when':'',
            'where':'',
            'description':''
        }
        fields = ['name', 'when', 'where', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'when': forms.DateInput(attrs={'placeholder': 'when: YYYY-MM-DD'}),
            'where': forms.TextInput(attrs={'placeholder': 'where'}),
            'description': forms.Textarea(attrs={'placeholder': 'description'})
        }
