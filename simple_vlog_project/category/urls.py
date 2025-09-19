from django.urls import path
from category.views import Add_Category

urlpatterns = [
   
    path('add/',Add_Category,name="add_category"),
  

]