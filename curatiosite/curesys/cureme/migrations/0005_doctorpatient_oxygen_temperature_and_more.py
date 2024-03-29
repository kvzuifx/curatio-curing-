# Generated by Django 5.0 on 2024-01-20 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cureme', '0004_doctorpatients'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorPatient',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'doctor_patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('oxygen_id', models.AutoField(primary_key=True, serialize=False)),
                ('oxygen_rate', models.IntegerField()),
                ('datetime', models.DateField()),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='cureme.patient')),
            ],
            options={
                'db_table': 'oxygen',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('temp_id', models.AutoField(primary_key=True, serialize=False)),
                ('temperature', models.IntegerField()),
                ('datetime', models.DateField()),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='cureme.patient')),
            ],
            options={
                'db_table': 'temperature',
            },
        ),
        migrations.DeleteModel(
            name='DoctorPatients',
        ),
    ]
