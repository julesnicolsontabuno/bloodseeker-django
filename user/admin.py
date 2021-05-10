from django.contrib import admin

# Register your models here.
from .models import User, Donor, RequestDonor

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(RequestDonor)
