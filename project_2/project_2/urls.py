
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contact/',views.Contact),
    path('second_app/',include('second_apps.urls')),
    path('',views.Home),

]
