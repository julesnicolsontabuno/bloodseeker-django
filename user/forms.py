from django import forms
from django.db.models import fields
from django.db.models.base import Model
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
        model = Donor
        fields = [
            "donorID",
            "address",
            "donorBloodType",
            "attachmentsDonor",
            "isApproved",
            "username",
       ]

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = [
            "hospitalName",
            "hospitalAddress",
            "businessEmail",
            "contactInfo",
            "attachmentsID",
            "isApproved",
            "oPlus",
            "oMinus",
            "aPlus",
            "aMinus",
            "bPlus",
            "bMinus",
            "aBPlus",
            "aBMinus",
            "username",
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "appointmentID",
            "appointmentType",
            "setDate",
            "setTime",
            "isApproved",
        ]

