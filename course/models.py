from django.db import models
from category.models import Category


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    logo = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name