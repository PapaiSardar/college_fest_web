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