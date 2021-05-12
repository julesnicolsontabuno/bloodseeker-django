from django.db import models

# Create your models here.

#GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
BLOODTYPE_CHOICES = [('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),]

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
    donor_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    donorBloodType = models.CharField(choices=BLOODTYPE_CHOICES, max_length=3)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class RequestDonor(models.Model):
    requestDonorID = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    donorBloodType = models.CharField(choices=BLOODTYPE_CHOICES, max_length=3)
    isApproved = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class RequestOrganizer(models.Model):
    requestOrganizerID = models.AutoField(primary_key=True)
    hospitalName = models.CharField(max_length=100)
    hospitalAddress = models.CharField(max_length=100)
    businessEmail = models.EmailField(max_length=100)
    contactInfo = models.CharField(max_length=11)
    isApproved = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)