
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View 
from .forms import UserRegistrationForm
from django.views.generic.edit import  UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile



class User_Registration(View):
    def get(self, request, *args, **kwargs):

        user_form = UserRegistrationForm()

        return render(request, 'user_account/registration.html', {'user_form': user_form})

    def post (self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)           
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
            user_profile = Profile(user = new_user)
            user_profile.save()
            return render(request, 'user_account/registration_done.html', {'new_user': new_user})
        else: 
            return render(request, 'user_account/registration.html', {'user_form': user_form})


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'date_of_birth', 'city', 'bio', 'profile_photo']
    template_name= 'user_account/profile_form.html'
    success_url = reverse_lazy('home')

    
class UserProfile(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        user = get_object_or_404(User,pk = kwargs.get("pk"))
        user_posts= user.user_posts.all()

        return render(request, "user_account/user_profile.html", {
            "profileUser": user,
            "user_posts": user_posts
        
        
        })


class Members(ListView):
    template_name = "user_account/members.html"
    model = User
    context_object_name = "members"
    paginate_by = 3

    def get_queryset(self):
        base_query =  super().get_queryset()

        if self.request.user.is_authenticated:
            data =  base_query.exclude(pk=self.request.user.pk)

            followers_list =  User.objects.get(pk=self.request.user.pk).profile.followers.all().values_list('pk', flat=True)
            data = data.exclude(id__in =followers_list )
            return data 



        return base_query


class AddFollower(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print(kwargs.get('pk'))

        followed_user = get_object_or_404(User, pk=kwargs.get('pk'))

        self.request.user.profile.followers.add(followed_user)

        return redirect("members")