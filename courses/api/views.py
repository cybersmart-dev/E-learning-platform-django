from rest_framework import generics
from courses.models import Student,Course
from courses.api.serializers import StudentSerializers,CourseSerializers
class StudentsApiView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class CoursesApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers    