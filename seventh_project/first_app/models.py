from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=50)


    def __str__(self):
        return f"name:{self.name}->Roll:{self.roll}"