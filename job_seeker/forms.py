from django import forms
from job_seeker.models import Application

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
        
    resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

