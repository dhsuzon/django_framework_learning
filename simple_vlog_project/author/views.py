from django.shortcuts import render,redirect
from author.forms import AuthorForm

# Create your views here.

def Add_Author(request):
    if request.method =="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_author')
    else:    
        form = AuthorForm()
    return render(request,'author/add_author.html',{'form':form})
