from django import forms
from .models import *

class DonorForm(forms.ModelForm):
    class Meta:
        model = RequestDonor
        fields = [
            "requestDonorID",
            "address",
            "donorBloodType",
            "isApproved",
            "username",
        ]

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = RequestOrganizer
        fields = [
            "requestOrganizerID",
            "hospitalName",
            "hospitalAddress",
            "businessEmail",
            "contactInfo",
            "isApproved",
            "username",
        ]