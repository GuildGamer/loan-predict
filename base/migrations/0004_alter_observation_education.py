# Generated by Django 3.2.6 on 2021-09-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_observation_loan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='Education',
            field=models.CharField(choices=[('Graduate', 'graduate'), ('Not Graduate', 'not_graduate')], max_length=12),
        ),
    ]
