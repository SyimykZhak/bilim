from django.urls import path
from . import views

urlpatterns=[
path('', views.CourseListView.as_view(), name='courses_list'),
path('teachers/', views.TeacherDetailView.as_view(), name='teachers'),
path('as/', views.primer, name='places_list'),
path('course/<str:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
path("teacher/<str:slug>/", views.TeacherView.as_view(), name="teacher_detail"),
]
