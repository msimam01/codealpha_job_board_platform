from django import forms
from employer.models import Job

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description", "company", "location", "deadline"]
        
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 5}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Deadline'}))
