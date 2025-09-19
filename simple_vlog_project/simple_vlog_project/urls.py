
from django.contrib import admin
from django.urls import path,include
from .views import Show_Post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include("author.urls")),
    path('profile/', include("profiles.urls")),
    path('post/', include("post.urls")),
    path('category/', include("category.urls")),
    path('',Show_Post,name="homepagepost"),

]
