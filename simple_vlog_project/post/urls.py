
from django.urls import path
from post.views import Add_Post,Edit_Post,Delete_Post

urlpatterns = [
   
    path('add/',Add_Post,name="add_post"),
    path('edit/<int:id>/',Edit_Post,name="edit_post"),
    path('delete/<int:id>/',Delete_Post,name="delete_post"),
]
