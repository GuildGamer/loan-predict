from django.db import models
from django.conf import settings

GENDER = (
   ( 'M', 'male'),
    ('F', 'female')
)

YES_OR_NO = (
    ('Y', 'yes'),
    ('N', 'no')
)

EDUCATION_STATUS = (
    ('GR', 'graduate'),
    ('NT', 'not')
)

PROPERTY_AREA = (
    ('UR', 'urban'),
    ('RU', 'rural')
)

class Observation(models.Model):
    loan_id= models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER, max_length=1)	
    married	= models.CharField(choices=YES_OR_NO, max_length=1)
    dependents = models.IntegerField()
    education = models.CharField(choices=EDUCATION_STATUS, max_length=2)
    self_employed = models.CharField(choices=YES_OR_NO, max_length=1)
    applicant_income = models.BigIntegerField() 
    loan_amount = models.BigIntegerField()
    loan_amount_term = models.BigIntegerField()	
    credit_history = models.FloatField()
    property_area = models.CharField(choices=PROPERTY_AREA, max_length=2)
    loan_status = models.CharField(choices=YES_OR_NO, max_length=1)
