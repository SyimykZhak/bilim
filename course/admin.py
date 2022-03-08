from django.contrib import admin
from .models import Courses, lessons, Teachers
from django.utils.safestring import mark_safe


class LessonsInline(admin.StackedInline):
    model = lessons
    extra = 1

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display =("name", "description", "draft")
    inlines = [LessonsInline]
    save_on_top = True
    # save_as = True
    list_editable = ("draft",)
    
    fieldsets = (
        (None,{
            "fields": ("name", "description", "teacher")
        }),
        (None,{
            "fields": (("term", "modul", "time"),)
        }),
        (None,{
            "fields": (("image","price"),)
        }),
        ("Options",{
            "fields": ("draft",)
        }),
    )

@admin.register(lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display =["title", "course_name", "description"]
    list_filter = ("course_name", "title")
    search_fields = ("title",)

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display =["name", "age", "get_image"]
    readonly_fields =("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Изображение"


