from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Teachers(models.Model):
    name = models.CharField("Имя", max_length=100)
    speciality = models.CharField("Специалность", max_length=20)
    age = models.PositiveIntegerField("Возраст", default=0)
    image = models.ImageField("Изображение")
    description = models.TextField("Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.name})
    
    class Meta:
        verbose_name = 'ментор'
        verbose_name_plural = 'менторы'
        ordering = ['name']


class Courses(models.Model):
    user = models.ForeignKey(to=User, 
    on_delete=models.SET_NULL,
    null=True, blank=True
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True,max_length=255, blank=True) #не обязвтельное поле
    teacher = models.ManyToManyField(Teachers, verbose_name="преподаватель", related_name="course_teachers")
    time = models.IntegerField("длительность одного урока",default=0)
    term = models.IntegerField("срок(в месяцах)",default=0)
    modul = models.IntegerField("модуль",default=0)
    created_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)
    draft = models.BooleanField("Опубликовать", default=False)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ['name']
        
    
class lessons(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="описание")
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="видео")
    course_name = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_name")
    added = models.DateTimeField(auto_now_add=True)
    task = models.URLField(verbose_name="ссылка к заданию", null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ['title']

