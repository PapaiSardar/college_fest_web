from django.db import models

# Create your models here.
class student_basic(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    payment_status=models.IntegerField()
    class Meta:
        db_table='student_basic'