from django.shortcuts import render
from .forms import Contact_Form,StudentData,PasswardMatchProject


def Home(request):
    return render(request,"firstapp/home.html")
def About(request):
    if request.method=="POST":
       name = request.POST.get('First_Name')
       email = request.POST.get('Email')
       select= request.POST.get('select')
       return render(request,"firstapp/about.html",{'name':name,'email':email,'select':select})   
    return render(request,"firstapp/about.html")  


def HTML_FORM(request):
    return render(request,"firstapp/forms.html") 

def DJANGO_FORM(request):
    if request.method=="POST":   
       form = Contact_Form(request.POST)
       if form.is_valid():
        print(form.cleaned_data)
        return render(request,"firstapp/djangobuiltform.html",{'form':form}) 
    else:   
      form = Contact_Form()   
    return render(request,"firstapp/djangobuiltform.html",{'form':form}) 

def Student_Data(request):
    if request.method=="POST":   
       form = StudentData(request.POST,request.FILES)
       if form.is_valid():
        print(form.cleaned_data)
        return render(request,"firstapp/studentdata.html",{'form':form}) 
    else:   
      form = StudentData()   
    return render(request,"firstapp/studentdata.html",{'form':form}) 



def Passward_Match_Project(request):
    if request.method=="POST":   
       form = PasswardMatchProject(request.POST,)
       if form.is_valid():
        print(form.cleaned_data)
        return render(request,"firstapp/passward_match.html",{'form':form}) 
    else:   
      form = PasswardMatchProject() 
    return render(request,"firstapp/passward_match.html",{'form':form})