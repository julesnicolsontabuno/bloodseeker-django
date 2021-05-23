from django.contrib import admin

# Register your models here.
from .models import User, RequestDonor, Organizer, RequestAppointment, Donor

admin.site.register(User)
admin.site.register(RequestDonor)
admin.site.register(Organizer)
admin.site.register(RequestAppointment)
admin.site.register(Donor)

