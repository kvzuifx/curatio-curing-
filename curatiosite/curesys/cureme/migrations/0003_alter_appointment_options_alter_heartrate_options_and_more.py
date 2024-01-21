# Generated by Django 5.0 on 2024-01-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cureme', '0002_allergy_diagnosis_doctor_test_vitalsign_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='heartrate',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='immunization',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='medication',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prescription',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='respirationrate',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='surgery',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='testappointment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='testreport',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='vitalsign',
            options={'managed': False},
        ),
    ]