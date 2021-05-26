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

class RequestDonorForm(forms.ModelForm):
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
            "organizerID",
            "hospitalName",
            "hospitalAddress",
            "businessEmail",
            "contactInfo",
            "attachmentsID",
            "isApproved",
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

