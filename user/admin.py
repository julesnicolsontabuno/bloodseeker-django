from django.contrib import admin

# Register your models here.
from .models import User, Donor, Organizer, Appointment

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Organizer)
admin.site.register(Appointment)


