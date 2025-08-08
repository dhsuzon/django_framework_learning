from django.shortcuts import render,HttpResponse

# Create your views here.

def Course(request):
    return HttpResponse("this is courses page")
