from django.db import models
from author.models import AuthorModel

class ProfileModel(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()
    author = models.OneToOneField(AuthorModel,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return F"profileName={self.name},authorName={self.author.name}"

