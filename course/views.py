from pyexpat import model
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Courses, Teachers, lessons
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class LessonsFilter:
    def get_courses(self):
        return Courses.objects.all()

    def get_lessons(self):
        return lessons.objects.filter(draft=False).values("course_name")

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
    
 
class TeacherDetailView(LoginRequiredMixin,ListView):
    model = Teachers
    template_name ='course/teachers.html'
    context_object_name = "teachers"
    raise_exception = True

class FilterLessonsView(LessonsFilter,ListView):
    def get_queryset(self):
        queryset = lessons.objects.filter(
            Q(course_name__in=self.request.GET.getlist("course_name"))
            )
        return queryset 