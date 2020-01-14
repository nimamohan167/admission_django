from django.db import models

#Faculty profile and registration

class faculty_profile(models.Model):
    faculty_id       = models.IntegerField(primary_key=True)
    name             = models.CharField(max_length=200)
    username         = models.CharField(max_length=200,unique=True)
    password         = models.CharField(max_length=200)
    designation      = models.CharField(max_length=200)
    join_date        = models.CharField(max_length=200)
    qualification    = models.CharField(max_length=200)
    gender           = models.CharField(max_length=200)
    mobile           = models.CharField(max_length=200)
    email            = models.CharField(max_length=200)
    batchincharge    = models.CharField(max_length=200)
    blood_grp        = models.CharField(max_length=200)
    dob              = models.CharField(max_length=200)
    address          = models.CharField(max_length=200)

    class Meta:
       db_table = 'faculty_profile'


class faculty_assessment(models.Model):
    roll_no          = models.IntegerField(primary_key=True)
    name             = models.CharField(max_length=200)
    batch            = models.CharField(max_length=200)
    asses1           = models.CharField(max_length=200)
    asses2           = models.CharField(max_length=200)
    asses3           = models.CharField(max_length=200)
    rank             = models.CharField(max_length=200)
    
    class Meta:
       db_table = 'faculty_assessment'

class faculty_attendence(models.Model):
    roll_no          = models.IntegerField(primary_key=True)
    name             = models.CharField(max_length=200)
    batch            = models.CharField(max_length=200)
    date             = models.CharField(max_length=200,blank=True)
    fhour            = models.CharField(max_length=200)
    shour            = models.CharField(max_length=200)
    thour            = models.CharField(max_length=200)
    fohour           = models.CharField(max_length=200,blank=True)
    
    class Meta:
       db_table = 'faculty_attendence'
