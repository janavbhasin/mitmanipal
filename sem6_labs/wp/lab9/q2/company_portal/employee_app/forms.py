from django import forms
from .models import WORKS

class WORKSForm(forms.ModelForm):
    class Meta:
        model = WORKS
        fields = ['person_name', 'company_name', 'salary']

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)
