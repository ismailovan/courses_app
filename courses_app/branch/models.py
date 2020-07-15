from django.db import models
from course.models import Course

# Create your models here.
class Branch(models.Model):
	latitude = models.CharField(max_length = 255)
	longtitude = models.CharField(max_length = 255)
	adress = models.CharField(max_length = 255)
	course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = "branches")

	def __str__(self):
		return self.adress