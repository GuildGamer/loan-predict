# Generated by Django 3.2.6 on 2021-09-01 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='Self_employed',
            new_name='Self_Employed',
        ),
    ]
