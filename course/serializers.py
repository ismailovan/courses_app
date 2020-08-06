from rest_framework import serializers
from .models import Course
from branch.models import Branch
from branch.serializers import BranchSerializer
from category.models import Category
from contact.models import Contact
from contact.serializers import ContactSerializer

class CourseSerializer(serializers.ModelSerializer):
	contacts = ContactSerializer(many = True)
	branches = BranchSerializer(many = True)
	category = serializers.PrimaryKeyRelatedField(
		queryset = Category.objects.all()
	)
	
	class Meta:
		model = Course
		fields = (
			
            "name",
            "description",
            "category",
            "logo",
            "contacts",
            "branches",
        )


	def create(self, validated_data):
		contact = validated_data.pop('contacts')
		branch = validated_data.pop('branches')

		course = Course.objects.create(**validated_data)

		for contact in contact:
			Contact.objects.create(course = course, **contact)
		for branch in branch:
			Branch.objects.create(course = course, **branch)
		return course

