from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "firstName",
            "lastName",
            "username",
            "email",
            "contactNumber",
            "age",
            "password",
            "gender"
        ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

class DonorForm(forms.ModelForm):
    class Meta:
        model = RequestDonor
        fields = [
            "requestDonorID",
            "address",
            "donorBloodType",
            "attachmentsDonor",
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
            "attachments",
            "isApproved",
            "username",
        ]