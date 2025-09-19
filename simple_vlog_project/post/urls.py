
from django.urls import path
from post.views import Add_Post

urlpatterns = [
   
    path('add/',Add_Post,name="add_post"),
]
