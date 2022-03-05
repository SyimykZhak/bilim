from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
# Create your models here.

class AboutUs(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("email",blank=True, null=True)
    telephone = models.CharField("Телефон", max_length=15)
    addres = models.CharField("Адрес", max_length=100)
    header = models.CharField("заголовок", max_length=100)
    description = models.TextField("Описание",max_length=10000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE,
        related_name='profile'
    )
    region = models.CharField(max_length=255,
    choices=(
        ('O','Osh'),
        ('B','Bishkek'),
        ('N','Naryn'),
        ('A','Alai'),
        ('T','Talas'),
        ('J','Jalal-Abad'),
    ))
    
    photo = ImageField(
        upload_to='profile_photo',
        null=True,blank=True
    )

    def __str__(self):
        return self.user.username