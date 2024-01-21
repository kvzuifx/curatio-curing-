from django.db import models
from django.contrib.auth.models import User
#
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    doctor_id = models.AutoField(primary_key=True)
    doctor_fname = models.CharField(max_length=255)
    doctor_lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    doctor_contact_no = models.BigIntegerField()
    address = models.CharField(max_length=255)
    license_no = models.BigIntegerField()
    specialty = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True)


    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return f"Doctor {self.doctor_id}: {self.doctor_fname} {self.doctor_lname}"


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    patient_fname = models.CharField(max_length=255)
    patient_lname = models.CharField(max_length=255)
    patient_id = models.AutoField(primary_key=True)
    patient_dob = models.DateField()
    patient_gender = models.CharField(max_length=1)
    patient_contact_no = models.BigIntegerField()
    emer_contact_name = models.CharField(max_length=255)
    emer_contact_no = models.BigIntegerField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True)

    class Meta:
            managed = False
            db_table = 'patient'
    
    def __str__(self):
        return f"Patient {self.patient_id}: {self.patient_fname} {self.patient_lname}"


class DoctorPatient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_id')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    id = models.AutoField(primary_key=True, db_column='Id')

    class Meta:
        managed= False
        db_table = 'doctor_patient'
    
    def __str__(self):
        return f'{self.patient}'


        

class Allergy(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    allergy_name = models.CharField(max_length=255)
    allergy_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    allergic_reaction = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'allergies'
        

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_id')
    status = models.CharField(null=True, blank=True,max_length=255)
    condition = models.CharField(null=True, blank=True,max_length=255)
    class Meta:
        managed = False
        db_table = 'appointment'
    def __str__(self):
        return f'{self.appointment_id}'

    
    
class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    date = models.DateField()
    diagnosis = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_id')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'diagnosis'
        
class HeartRate(models.Model):
    heart_rate_id = models.AutoField(primary_key=True)
    datetaken = models.DateField()
    heart_rate = models.IntegerField()
    comments = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'heart_rate'

class Immunization(models.Model):
    immu_id = models.AutoField(primary_key=True)
    immu_name = models.CharField(max_length=255)
    datetime = models.DateField()
    status = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'immunizations'

class Medication(models.Model):
    medications_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'medications'
        

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_id')
    duration = models.CharField(max_length=255)
    dosage=models.CharField(max_length=255)
    medications = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'prescription'
    def __str__(self):
        return f'Patient Medication is {self.medications}'

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    report_type = models.CharField(max_length=255)
    report_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report'

class RespirationRate(models.Model):
    resp_rate_id = models.AutoField(primary_key=True)
    datetaken = models.DateField()
    resp_rate = models.IntegerField()
    comments = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'respiration_rate'

class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=255)
    surgeon = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        managed = False
        db_table = 'surgery'
        
class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    test_description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'test'
        
    def __str__(self):
        return self.test_name


class TestReport(models.Model):
    test_report_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    test_type = models.ForeignKey(Test, on_delete=models.CASCADE, db_column='test_type_id')
    test_report_date = models.DateField()
    test_report_file = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_id')

    class Meta:
        managed = False
        db_table = 'test_report'

class VitalSign(models.Model):
    vitalsign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vitalsign'
        
        
class BloodPressure(models.Model):
    blood_press_id = models.AutoField(primary_key=True)
    datetime = models.DateField()
    blood_press = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        db_table = 'blood_pressure'
    def __str__(self):
        return f'Patient {self.patient}: Blood Pressure is {self.blood_press}'      
    
class Oxygen(models.Model):
    oxygen_id = models.AutoField(primary_key=True)
    oxygen_rate = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    datetime = models.DateField()

    class Meta:
        db_table = 'oxygen'
    def __str__(self):
        return f'Patient {self.patient}: Oxygen rate is {self.oxygen_rate}'
    

class Temperature(models.Model):
    temp_id = models.AutoField(primary_key=True)
    temperature = models.IntegerField()
    datetime = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')

    class Meta:
        db_table = 'temperature'
    def __str__(self):
        return f'Patient {self.patient}: Temperature is {self.temperature}'
    
class Room(models.Model):
    room_number = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    loc_name = models.CharField(primary_key=True, max_length=255)
    class Meta:
        db_table = 'rooms'
    def __str__(self):
        return self.room_number
    
    
class TestAppointment(models.Model):
    test_appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, db_column='test_id')
    appointment_datetime = models.DateField()
    location = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='location', to_field='loc_name')
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'test_appointment'
    def __str__(self):
        return f'Patient Test Appointment is {self.test} at {self.location}'
