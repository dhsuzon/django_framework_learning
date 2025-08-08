from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request,'navigation_two/About.html')

def Contact(request):
    return render(request,'navigation_two/Contact.html')
