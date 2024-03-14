from django.db import models

# Create your models here.
class student_detalis(models.Model): 
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    collage_status=models.IntegerField()
    college_name=models.CharField(max_length=300)
    payment_status=models.IntegerField()

    class Meta:
        db_table='student_detalis'



class admin(models.Model):
    user=models.CharField(max_length=50)
    pwd=models.IntegerField()
    class Meta:
        db_table='admin'


class events_detalis(models.Model):
    roll=models.IntegerField()
    event_name=models.CharField(max_length=100)
    part_no=models.IntegerField()
    class Meta:
        db_table='event_detalis'
class event(models.Model):
    roll=models.IntegerField()
    eventName=models.CharField(max_length=100)
    class Meta:
        db_table='event'

class abc(models.Model):
    roll = models.IntegerField()
    CatWalk = models.IntegerField(default=0)
    DuoDance = models.IntegerField(default=0)
    mintoframe = models.IntegerField(default=0)
    Facepaint = models.IntegerField(default=0)
    rell = models.IntegerField(default=0)
    selfie = models.IntegerField(default=0)

    class Meta:
        db_table = 'abc'