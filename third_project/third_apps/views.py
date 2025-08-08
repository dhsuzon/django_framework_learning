from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request):
   return render(request,'third_apps/home.html')
