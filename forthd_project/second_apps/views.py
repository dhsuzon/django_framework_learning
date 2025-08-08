from django.shortcuts import render
from datetime import datetime
# Create your views here.
def Home(request):
    d = {'author':"suzon","age":15,'lst':['python',"is","best"],'birthday':datetime.now,'course':[
        {'id':1,"name":"Python"}
        ,{'id':2,"name":"C"},
        {'id':3,"name":"Java"}
        ]}
    return render(request,"home.html",d)
