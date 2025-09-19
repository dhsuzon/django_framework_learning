from django.shortcuts import render,redirect
from  post.models import PostModel

def Show_Post(request):
    PostData = PostModel.objects.all()
    return render(request,'home.html',{"PostData":PostData})