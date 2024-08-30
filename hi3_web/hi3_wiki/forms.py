from django import forms

class search_weapons(forms.Form):
    query = forms.CharField(label='Search Weapons', max_length=100, required=False)