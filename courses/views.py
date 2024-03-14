from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.http import JsonResponse,HttpResponseRedirect
from .models import Course,Student
from django.urls import reverse
import json

# Create your views here.

def remove(request,username,title):
    student = get_object_or_404(Student,username=username)
    course = get_object_or_404(Course,title=title)
    course.students.remove(student)
    return HttpResponseRedirect(reverse('courses:student',args=[
        username
        ]))
def student(request,username):
    student = get_object_or_404(Student,username=username)
    all_courses = student.students.all()
    
    context = {
        'courses':all_courses,
        'student':student
    }
    
    return render(request,'student.html',context)
def enrolled(request,username,title):
    course = get_object_or_404(Course,title=title)
    student = get_object_or_404(Student,username=username)
    
    context = {
        'course':course,
        'student':student
    }
    return render(request,'enrolled.html',context)
    
def dashboard(request,username):
    student = get_object_or_404(Student,username=username)
    return HttpResponse(f'student {student.email}')
    
def start(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        is_exists = Student.objects.filter(email=email).exists()
        if is_exists:
            response = redirect('courses:index')
            student = Student.objects.get(email=email)
            response.set_cookie('email',email)
            response.set_cookie('uname',student.username)
            return response
        else:
            get_username = email.split("@")[0]
            username = f'@{get_username}'
            
            Student.objects.create(
                name = get_username,
                email=email,
                username = username
            )
            response = redirect('courses:index')
            response.set_cookie('uname',username)
            response.set_cookie('email',email)
        return response
    return render(request, 'start.html')
def about(request):
    
    response = redirect('courses:index')
    response.delete_cookie('email')
    return response
def index(request):
    courses = Course.objects.all()
    
    context = {
        'courses':courses
    }
    
    return render(request, 'index.html',context)

def courses_details(request, pk):
    course = get_object_or_404(Course,id=pk)
    is_ajax = request.headers.get("from") == "ajax"
    print(is_ajax)
    
    if is_ajax :
        student_email = request.COOKIES.get('email')
        if(student_email is not None):
            # data = json.dumps({"message":200})
            student = Student.objects.get(email=student_email)
            add = course.students.add(student)
            print(add)
            return JsonResponse({"message":200})
        else:
            # data = json.dumps({"message":404})
            return JsonResponse({"message":404})
    if request.method == "POST":
        email = request.POST.get("email")
        # course= request.POST.get("course")
        skill = 'None'
        student = Student.objects.filter(email=email)
        if(student.exists()):
            print("welcome Back")
            response = HttpResponseRedirect(reverse('courses:index'))
            student = Student.objects.get(email=email)
            course.students.add(student)
            response.set_cookie('email',student.email)
            response.set_cookie('uname',student.username)
            return response
        else:
            get_username = email.split("@")[0]
            username = f'@{get_username}'
            Student.objects.create(name=get_username,email=email,username=username,skill=skill)
            response = response = HttpResponseRedirect(reverse('courses:index'))
            response.set_cookie('email',email)
            response.set_cookie('uname',username)
            return response
    context = {
        'course':course
    }
    response = render(request, 'courses_details.html',context)
    return response