from django.shortcuts import render,redirect
from post.forms import PostForm
from post.models import PostModel

# Create your views here.

def Add_Post(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data["title"])
            return redirect('add_post')
    else:    
        form = PostForm()
    return render(request,'post/add_post.html',{'form':form})

def Edit_Post(request,id):
    post = PostModel.objects.get(id=id)
    if request.method =="POST":
        
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=True)
            return redirect('homepagepost')
    else:    
        form = PostForm(instance=post)
    return render(request,'post/edit_post.html',{'form':form})



def Delete_Post(request,id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return redirect("homepagepost")
    # if request.method =="POST":
        
    #     form = PostForm(request.POST, instance=post)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         print(form.cleaned_data["title"])
    #         return redirect('homepagepost')
    # else:    
    #     form = PostForm(instance=post)
    # return render(request,'post/edit_post.html',{'form':form})





