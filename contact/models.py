from django.db import models
from course.models import Course

# Create your models here.
class Contact(models.Model):   

    CONTACT = [
        (1, 'Phone'),
        (2, 'Email'),
        (3, 'Facebook')
    ]
    contact_type = models.IntegerField(choices = CONTACT)
    value = models.CharField(max_length = 255)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = "contacts")
    
    def __str__(self):
        return self.value