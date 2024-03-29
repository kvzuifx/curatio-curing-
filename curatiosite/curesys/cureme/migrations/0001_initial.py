# Generated by Django 5.0 on 2024-01-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_fname', models.CharField(max_length=255)),
                ('patient_lname', models.CharField(max_length=255)),
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_dob', models.DateField()),
                ('patient_gender', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('patient_contact_no', models.BigIntegerField()),
                ('emer_contact_name', models.CharField(max_length=255)),
                ('emer_contact_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
