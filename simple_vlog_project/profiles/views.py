from django.shortcuts import render
from profiles.forms import ProfileForm

# Create your views here.
def Add_Profile(request):
    if request.method =="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data["name"])
            return render(request,'profile/add_profile.html',{'form':form})
    else:    
        form =ProfileForm()
    return render(request,'profile/add_profile.html',{'form':form})
