from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views 


urlpatterns = [
    path('register/', views.User_Registration.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path ('logout/',auth_views.LogoutView.as_view(), name='logout' ),
    path('<int:pk>/updateProfile/', views.UpdateProfile.as_view(), name='update_profile'),
    path('<int:pk>/userProfile/',views.UserProfile.as_view(), name='user_profile'),
    path('members/', views.Members.as_view(), name='members'),
    path('<int:pk>/addFollower/', views.AddFollower.as_view(), name= 'add_follower' )
]