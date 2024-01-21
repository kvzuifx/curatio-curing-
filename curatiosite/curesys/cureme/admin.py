from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(DoctorPatient)
admin.site.register(Allergy)
admin.site.register(Appointment)
admin.site.register(BloodPressure)
admin.site.register(Diagnosis)
admin.site.register(Medication)
admin.site.register(Immunization)
admin.site.register(HeartRate)
admin.site.register(Prescription)
admin.site.register(Report)
admin.site.register(RespirationRate)
admin.site.register(Surgery)
admin.site.register(Oxygen)
admin.site.register(Temperature)

##
admin.site.register(Test)
admin.site.register(TestAppointment)
admin.site.register(Room)
