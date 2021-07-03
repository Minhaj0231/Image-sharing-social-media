from django.urls import path

from . import views 

app_name = "post"

urlpatterns = [
    path('addPost/', views.Add_Post.as_view(), name='addPost'),
    
]