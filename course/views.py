from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Courses, Teachers
from django.contrib.auth.mixins import LoginRequiredMixin


def primer(request):
    return HttpResponse('primer')
    
class CourseListView(ListView):
    model = Courses
    template_name = "course/courses.html"
    context_object_name = "courses"
    paginate_by = 2
    
    

class CourseDetailView(LoginRequiredMixin,DetailView):
    model = Courses
    template_name = "course/course.html"
    context_object_name = "course"
    slug_field = "name"
    paginate_by = 4
    
 
class TeacherDetailView(ListView):
    model = Teachers
    template_name ='course/teachers.html'
    context_object_name = "teachers"
    paginate_by = 4



class TeacherView(LoginRequiredMixin,DetailView):
    model = Teachers
    template_name = 'course/teacher.html'
    context_object_name = "teacher"
    slug_field = "name"
    raise_exception = True
