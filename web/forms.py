from django import forms

CHOICES = [('select1', 'select 1'),
           ('select2', 'select 2')]

like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
