from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import  Post, Comment


class Add_Post(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'post_image', 'tags']

    template_name =  "post/addPost.html"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form) :
        data = form.save(commit=False)
        data.user = self.request.user
        
        data.save()

        for item in form.cleaned_data["tags"]:
            data.tags.add(str(item))
        


        print(self.request.user.id)
        return redirect("user_profile", self.request.user.id)