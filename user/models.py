from tkinter import CASCADE
from django.db import models

# Create your models here.

#GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
BLOODTYPE_CHOICES = [('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),]
APPOINTMENT_CHOICES = [('Requesting for Blood Donation', 'Requesting for Blood Donation'), ('Requesting for Immediate Transfusion','Requesting for Immediate Transfusion')]
STATUS_CHOICES = [('Ready to Donate', 'Ready to Donate'), ('Has Donated', 'Has Donated'), ('Waiting Appointment', 'Waiting Appointment')]

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contactNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

class Donor(models.Model):
    donorID = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    donorBloodType = models.CharField(choices=BLOODTYPE_CHOICES, max_length=3)
    attachmentsDonor = models.FileField()
    isApproved = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Organizer(models.Model):
    hospitalName = models.CharField(max_length=100, primary_key=True)
    hospitalAddress = models.CharField(max_length=100)
    businessEmail = models.EmailField(max_length=100)
    contactInfo = models.CharField(max_length=20)
    attachmentsID = models.FileField()
    isApproved = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class BloodBank(models.Model):
    bloodBankID = models.AutoField(primary_key=True)
    oPlus = models.CharField(max_length=100)
    oMinus = models.CharField(max_length=100)
    aPlus = models.CharField(max_length=100)
    aMinus = models.CharField(max_length=100)
    bPlus = models.CharField(max_length=100)
    bMinus = models.CharField(max_length=100)
    aBPlus = models.CharField(max_length=100)
    aBMinus = models.CharField(max_length=100)
    hospitalName = models.ForeignKey(Organizer, on_delete=models.CASCADE)

class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    appointmentType = models.CharField(choices=APPOINTMENT_CHOICES, max_length=100)
    setDate = models.DateField()
    setTime = models.TimeField()
    isApproved = models.BooleanField(default=False)
    donorID = models.ForeignKey(Donor, on_delete=models.CASCADE)





    




