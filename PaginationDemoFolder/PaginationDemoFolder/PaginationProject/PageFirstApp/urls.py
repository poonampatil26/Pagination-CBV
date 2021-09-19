from django.urls import path
from .views import StudentList

urlpatterns = [
    path('cbvstu/',StudentList.as_view(), name='cbvstu'),
]