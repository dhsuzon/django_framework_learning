from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.Home,name="homepage"),
    path('about/',views.About,name="aboutpage"),
    path('html_form/',views.HTML_FORM,name="htmlformspage"),
    path('django_bulit_in_form/',views.DJANGO_FORM,name="djangobulitinform"),
    path('django_bulit_in_form_costome_validate/',views.Student_Data,name="djangobulitinformcostomevalidate"),
    path('Passward_Match_Project/',views.Passward_Match_Project,name="Passward_Match_Project"),
]
