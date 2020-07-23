from django.urls import path
from course import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('course/', views.CourseList.as_view(), name = 'courseList'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name = 'courseDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
