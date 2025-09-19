from django.db import models

# creating a model object

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="suzon")


    def __str__(self):
        return f"name={self.name}->roll={self.roll}"


