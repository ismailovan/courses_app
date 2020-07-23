import json
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from course.models import Course
from course.serializers import CourseSerializer
from branch.models import Branch
from category.models import Category
from contact.models import Contact

client = APIClient()

class GetAllCoursesTest(TestCase):
    
	def setUp(self):
		category = Category.objects.create(name = "Test category", imgpath = "Test image")
		course = Course.objects.create(name = "Test name", description = "Test description", logo = "Test logo", category = category)
		course1 = Course.objects.create(name = "Test name1", description = "Test description1", logo = "Test logo1", category = category)
		course2 = Course.objects.create(name = "Test name2", description = "Test description2", logo = "Test logo2", category = category)
		contact = Contact.objects.create(contact_type = 1, value = "Test value", course = course)
		branch = Branch.objects.create(latitude = "Test latitude", longtitude = "Test longtitude", adress = "Test adress", course = course)
		contact1 = Contact.objects.create(contact_type = 2, value = "Test value1", course = course1)
		branch1 = Branch.objects.create(latitude = "Test latitude1", longtitude = "Test longtitude1", adress = "Test adress1", course = course1)
		contact2 = Contact.objects.create(contact_type = 3, value = "Test value2", course = course2)
		branch3 = Branch.objects.create(latitude = "Test latitude2", longtitude = "Test longtitude2", adress = "Test adress2", course = course2)
		
	def test_get_all_courses(self):
		response = client.get(reverse('courseList'))
		course_list = Course.objects.all()
		serializer = CourseSerializer(course_list, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewCourseTest(TestCase):
    
	def setUp(self):
		self.category = Category.objects.create(name = "Test category", imgpath = "Test image")
		self.valid_data = {
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
		self.invalid_data = {
					"name": "",
					"description": "Test description",
					"logo": "",
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

	def test_create_valid_course(self):
		response = client.post(reverse('courseList'),
		data = json.dumps(self.valid_data),
		content_type = 'application/json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_course(self):
		response = client.post(reverse('courseList'),
		data = json.dumps(self.invalid_data),
		content_type = 'application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSingleCourseTest(TestCase):
    
	def setUp(self):
		self.category = Category.objects.create(name = "Test category", imgpath = "Test image")
		self.course = Course.objects.create(name = "Test name", description = "Test description", logo = "Test logo", category = self.category)
		self.course1 = Course.objects.create(name = "Test name1", description = "Test description1", logo = "Test logo1", category = self.category)
		self.course2 = Course.objects.create(name = "Test name2", description = "Test description2", logo = "Test logo2", category = self.category)
		self.contact = Contact.objects.create(contact_type = 1, value = "Test value", course = self.course)
		self.branch = Branch.objects.create(latitude = "Test latitude", longtitude = "Test longtitude", adress = "Test adress", course = self.course)
		self.contact1 = Contact.objects.create(contact_type = 2, value = "Test value1", course = self.course1)
		self.branch1 = Branch.objects.create(latitude = "Test latitude1", longtitude = "Test longtitude1", adress = "Test adress1", course = self.course1)
		self.contact2 = Contact.objects.create(contact_type = 3, value = "Test value2", course = self.course2)
		self.branch3 = Branch.objects.create(latitude = "Test latitude2", longtitude = "Test longtitude2", adress = "Test adress2", course = self.course2)
		
	def test_get_valid_single_course(self):
		response = client.get(reverse('courseDetail', kwargs={'pk': self.course1.pk}))
		course = Course.objects.get(pk=self.course1.pk)
		serializer = CourseSerializer(course)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_course(self):
		response = client.get(
		reverse('courseDetail', kwargs={'pk': 30}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_valid_delete_course(self):
		response = self.client.delete(reverse('courseDetail', kwargs={'pk': self.course1.pk}))
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_puppy(self):
		response = client.delete(reverse('courseDetail', kwargs={'pk': 30}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

