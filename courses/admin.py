from django.contrib import admin
from .models import Student,Course
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','created']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','skill','email']