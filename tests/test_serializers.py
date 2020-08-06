from django.test import TestCase
from course import serializers, models
from course.models import Course
from branch.models import Branch
from category.models import Category
from contact.models import Contact


class CoursesSerializerTest(TestCase):
	def setUp(cls):
		category = Category.objects.create(name = "Test category", imgpath = "Test image")
			
	def test_serializer_create(self):
		serializer_data = {
			"name": "Test name",
			"description": "Test description",
			"logo": "Test logo",
			"category": 1,
			"contacts": [
			        {
			        	"contact_type": 1,
			        	"value": "Test value"
			        }
			    ],
			"branches": [
			        {
			            "latitude": "Test latitude",
			            "longtitude": "Test longtitude",
			            "adress": "Test adress"
			        }
			    ]
			}			

		serializer = serializers.CourseSerializer(data = serializer_data)
		serializer.is_valid(raise_exception = True)
		serializer.save()

			
		self.assertIsNotNone(Course.objects.get(id = 1))