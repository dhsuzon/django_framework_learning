from django.db import models

class AuthorModel(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.name}"