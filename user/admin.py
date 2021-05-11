from django.contrib import admin

# Register your models here.
from .models import User, Donor, RequestDonor, RequestOrganizer

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(RequestDonor)
admin.site.register(RequestOrganizer)
