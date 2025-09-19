from django.shortcuts import render
from post.forms import PostForm

# Create your views here.

def Add_Post(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data["title"])
            return render(request,'post/add_post.html',{'form':form})
    else:    
        form = PostForm()
    return render(request,'post/add_post.html',{'form':form})
