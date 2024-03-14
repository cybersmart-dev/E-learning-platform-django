from rest_framework import serializers
from courses.models import Student,Course

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','email']
        
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','author','students','title','description','created']