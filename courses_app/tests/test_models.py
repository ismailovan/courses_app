from django.test import TestCase
from course.models import Course
from branch.models import Branch
from category.models import Category
from contact.models import Contact

class CourseTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		category = Category.objects.create(name = "Test category", imgpath = "Test image")
		course = Course.objects.create(name = "Test name", description = "Test description", logo = "Test logo", category = category)
		contact = Contact.objects.create(contact_type = 1, value = "Test value", course = course)
		branch = Branch.objects.create(latitude = "Test latitude", longtitude = "Test longtitude", adress = "Test adress", course = course)
	
	def test_category(self):
		category = Category.objects.get(id = 1)
		field_label_name = category.name
		field_label_image = category.imgpath
		self.assertEquals(field_label_name, "Test category")
		self.assertEquals(field_label_image, "Test image")

	def test_course(self):
		course = Course.objects.get(id = 1)
		field_label_name = course.name
		field_label_description = course.description
		field_label_logo = course.logo
		self.assertEquals(field_label_name, 'Test name')
		self.assertEquals(field_label_description, 'Test description')
		self.assertEquals(field_label_logo, 'Test logo')

	def test_contact(self):
		contact = Contact.objects.get(id = 1)
		field_label_value = contact.value
		self.assertEquals(field_label_value, 'Test value')

	def test_branch(self):
		branch = Branch.objects.get(id = 1)
		field_label_latitude = branch.latitude
		field_label_longtitude = branch.longtitude
		field_label_adress = branch.adress
		self.assertEquals(field_label_latitude, 'Test latitude')
		self.assertEquals(field_label_longtitude, 'Test longtitude')
		self.assertEquals(field_label_adress, 'Test adress')
