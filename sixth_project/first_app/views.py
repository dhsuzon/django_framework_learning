from django.shortcuts import render,redirect

from .models import Student

# Create your views here.
def Home(request):
    
    AllStudent = Student.objects.all()
    return render(request,'first_app/home.html',{'data':AllStudent})



def delete_student(request,Roll):
    
    sinlestudent = Student.objects.get(pk=Roll)
    sinlestudent.delete()
    return redirect("home")
    
    



    

    
    