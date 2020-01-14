from django.db import models
# Create your models here.

class student_reg(models.Model):
    admission_no     = models.IntegerField(primary_key=True)
    name             = models.CharField(max_length=200)
    roll_no          = models.CharField(max_length=200)
    qualification    = models.CharField(max_length=200)
    gender           = models.CharField(max_length=200)
    course           = models.CharField(max_length=200)
    batch            = models.CharField(max_length=200)
    dob              = models.CharField(max_length=200)
    admissn_date     = models.CharField(max_length=200,null=True)
    blood_grp        = models.CharField(max_length=200)
    mobile           = models.CharField(max_length=200)
    email            = models.CharField(max_length=200)
    address          = models.CharField(max_length=200,null=True)
    religion         = models.CharField(max_length=200)
    category         = models.CharField(max_length=200)
    username         = models.CharField(max_length=200,unique=True)
    password         = models.CharField(max_length=200)
    
    class Meta:
       db_table = 'student_registration'

class student_leave(models.Model):
    leave_id        = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=200)
    batch           = models.CharField(max_length=200,default='JSD2')
    from_date       = models.CharField(max_length=200)
    to_date         = models.CharField(max_length=200)
    reason          = models.CharField(max_length=200)
    describ         = models.CharField(max_length=200)
    status          = models.CharField(max_length=200,default='pending')
    

    class Meta:
       db_table = 'student_leave'
