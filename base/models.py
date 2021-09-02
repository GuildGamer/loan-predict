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
    ('Not Graduate', 'not_graduate')
)

class Observation(models.Model):
    Loan_ID= models.CharField(max_length=255)
    Gender = models.CharField(choices=GENDER, max_length=6)	
    Married	= models.CharField(choices=YES_OR_NO, max_length=3)
    Dependents = models.IntegerField()
    Education = models.CharField(choices=EDUCATION_STATUS, max_length=12)
    Self_Employed = models.CharField(choices=YES_OR_NO, max_length=3)
    ApplicantIncome = models.BigIntegerField() 
    CoapplicantIncome = models.BigIntegerField() 
    LoanAmount = models.BigIntegerField()
    Loan_Amount_Term = models.BigIntegerField()	
    Credit_History = models.FloatField()

    def __str__(self):
        return self.Loan_ID
        
