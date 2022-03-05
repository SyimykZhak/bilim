from django.contrib import admin
from .models import Courses, lessons
# Register your models here.

@admin.register(Courses)
class MovieAdmin(admin.ModelAdmin):
    list_display =["name","description", "draft"]
    list_editable = ("draft",)


admin.site.register(lessons)