from django.shortcuts import HttpResponse

def Contact(request):
    return HttpResponse("this  contact page")

def Home(request):
    return HttpResponse("this is home page")