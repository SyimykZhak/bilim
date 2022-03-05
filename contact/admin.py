from django.contrib import admin
from .models import Contacts
# Register your models here.
@admin.register(Contacts)
class MovieAdmin(admin.ModelAdmin):
    list_display =("name","email", "telephone")
    readonly_fields = ("name", "email")
