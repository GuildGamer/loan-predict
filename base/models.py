from django.db import models
from django.conf import settings

GENDER = (
   ( 'Male', 'male'),
    ('Female', 'female')
)

YES_OR_NO = (
    ('Yes', 'yes'),
    ('No', 'no')
)

EDUCATION_STATUS = (
    ('Graduate', 'graduate'),
    ('Not', 'not')
)

PROPERTY_AREA = (
    ('Urban', 'urban'),
    ('Rural', 'rural')
)

class Observation(models.Model):
    Loan_ID= models.CharField(max_length=255)
    Gender = models.CharField(choices=GENDER, max_length=6)	
    Married	= models.CharField(choices=YES_OR_NO, max_length=3)
    Dependents = models.IntegerField()
    Education = models.CharField(choices=EDUCATION_STATUS, max_length=8)
    Self_Employed = models.CharField(choices=YES_OR_NO, max_length=3)
    ApplicantIncome = models.BigIntegerField() 
    CoapplicantIncome = models.BigIntegerField() 
    LoanAmount = models.BigIntegerField()
    Loan_Amount_Term = models.BigIntegerField()	
    Credit_History = models.FloatField()
    Property_Area = models.CharField(choices=PROPERTY_AREA, max_length=5)

    def __str__(self):
        return self.Loan_ID
        
