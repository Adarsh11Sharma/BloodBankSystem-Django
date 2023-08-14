from django import forms
from django.contrib.auth.models import User
from . import models
from django.core.exceptions import ValidationError

class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['bloodgroup','address','mobile','profile_pic']

class DonationForm(forms.ModelForm):
    class Meta:
        model=models.BloodDonate
        fields=['age','bloodgroup','disease','unit']

    def clean_disease(self):
        data = self.cleaned_data['disease']
        if data.lower() in ['hiv','aids','blood pressure']  : 
            raise ValidationError("You can't donate blood, thank you!")
        return data

    def clean_age(self):
        data = self.cleaned_data['age']
        if data <18   : 
            raise ValidationError("You are below the age limit.")
        if data >60  : 
            raise ValidationError("You are above the age limit.")
        return data
