# Generated by Django 3.2.6 on 2021-09-01 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_self_employed_observation_self_employed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='Loan_Status',
        ),
    ]
