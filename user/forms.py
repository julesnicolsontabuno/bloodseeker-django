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