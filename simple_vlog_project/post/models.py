from django.db import models
from category.models import CategoryModel
from author.models import AuthorModel

class PostModel(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    Category = models.ManyToManyField(CategoryModel)
    Author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"title={self.title},author={self.Author.name}"





