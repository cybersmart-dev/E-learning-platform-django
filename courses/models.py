from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default="",blank=True,null=True)
    email = models.EmailField(max_length=200,unique=True)
    skill = models.CharField(max_length=200)
    
class Course(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = 'author'
        )
    students = models.ManyToManyField(Student,symmetrical=False,blank=True,null=True,related_name = 'students')    
    title = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to="static/courses/images/%y/%m/%d",default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def build_absolute_url(self):
        return reverse('courses:courses_details',
            args = [
                self.id
                ]
        )
    class Meta:
        ordering = ('-id',)