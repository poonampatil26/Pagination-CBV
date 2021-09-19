from django.shortcuts import render
from django.views import generic
from .models import Student

class StudentList(generic.ListView):
    queryset = Student.objects.all()
    template_name = 'PageFirstApp/Student_list.html'
    paginate_by = 3
