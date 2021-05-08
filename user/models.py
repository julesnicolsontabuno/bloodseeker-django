from django.db import models

# Create your models here.

GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
BLOODTYPE_CHOICES = [('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),]

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contactNumber = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    donorBloodType = models.CharField(choices=BLOODTYPE_CHOICES, max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
