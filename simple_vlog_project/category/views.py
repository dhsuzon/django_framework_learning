from django.shortcuts import render,redirect
from category.forms import CategoryForm

# Create your views here.

def Add_Category(request):
    if request.method =="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_category')
    else:    
        form = CategoryForm()
    return render(request,'category/add_category.html',{'form':form})
