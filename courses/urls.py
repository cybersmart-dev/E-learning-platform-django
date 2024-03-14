from django.urls import path
from .views import index,courses_details,about,start,dashboard,enrolled,student,remove

app_name = 'courses'

urlpatterns = [
  path('',index, name='index')  ,
  path('start/',start,name='start'),
  path('about/',about,name='about'),
  path('<str:username>/',student,name='student'),
  path('student/<str:username>/',dashboard, name='dashboard'),
  path('course/<int:pk>/',courses_details, name='courses_details'),
  path('remove/<str:username>/<str:title>/',remove,name='remove'),
  path("enrolled/<str:username>/<str:title>/",enrolled, name='enrolled')
]