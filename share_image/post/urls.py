from django.urls import path

from . import views 

app_name = "post"

urlpatterns = [
    path('addPost/', views.Add_Post.as_view(), name='addPost'),
    path('<int:pk>/postDetail/', views.Post_Detail.as_view(), name = 'postDetail'),
    path('/addComment', views.Add_Comment.as_view(), name = "addcomment"),
    path('/addLike', views.Add_Like.as_view(), name = "addLike")
]