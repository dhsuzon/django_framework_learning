
from django.urls import path
from . views import Home,delete_student

urlpatterns = [
   
    path('',Home,name="home"),
    path('student/delete/<int:Roll>/',delete_student,name="delStudent"),
    
]
