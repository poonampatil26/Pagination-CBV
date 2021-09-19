from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list = ['id','name','brance','age','grade']

admin.site.register(Student, StudentAdmin)