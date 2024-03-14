from .views import StudentsApiView,CoursesApiView
from django.urls  import path
app_name = 'api_courses'
urlpatterns = [
    path('list/',StudentsApiView.as_view()),
    path('courses_list/',CoursesApiView.as_view())
]