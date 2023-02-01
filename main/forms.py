from django import forms

from main.models import ValueForInput


class ValueForm(forms.Form):
    value = forms.CharField(label='Value', max_length=250)
