
from django.forms import ModelForm,formset_factory,inlineformset_factory
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateFormUser(UserCreationForm):
    class Meta:
        model =User
        fields = ['username', 'email','password1','password2']
        

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_fname', 'patient_lname', 'patient_dob', 'patient_gender',
                   'patient_contact_no', 'emer_contact_name',
                  'emer_contact_no', 'address']
        
        
class Patient(forms.ModelForm):

        class Meta:
            model = Patient
            fields = '__all__'
            exclude = ['user']
 
class BloodPressureForm(forms.ModelForm):
       class Meta:
           model= BloodPressure
           exclude = ['patient','blood_press_id']
           

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'doctor', 'condition']
