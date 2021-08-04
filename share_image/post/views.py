from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import  Post, Comment

from activity.models import Activity

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
        

        activity = Activity(user =  self.request.user, action = "posted", target = data )
        activity.save()    


        return redirect("user_profile", self.request.user.id)

class Post_Detail(View):
    def get(self, request,  *args, **kwargs):

        post_detail = get_object_or_404(Post,pk =kwargs.get("pk"))
        post_tags_ids = post_detail.tags.values_list('id', flat=True)

        post_comments = Comment.objects.filter(post = kwargs.get("pk"), restricted = False)
        

        similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post_detail.id).distinct()
        
        return render(request, "post/post_detail.html", {"post":post_detail , 
                                "similar_posts" : similar_posts,
                                "comments": post_comments
                                })

class Add_Comment(LoginRequiredMixin,View):
    def post(self, request,  *args, **kwargs):

        post_of_the_comment = get_object_or_404(Post, pk = request.POST["post_id"] )

        comment_obj = Comment( post = post_of_the_comment, 
                                comment_user = self.request.user,
                                comment_body= request.POST["comment"] )

        comment_obj.save()


        activity = Activity(user =  self.request.user, action = "commented on", target = post_of_the_comment  )
        activity.save()    

        return redirect('post:postDetail', request.POST["post_id"])

class Add_Like(LoginRequiredMixin,View):
    def post(self, request,  *args, **kwargs):
       
        
        

        post_obj = get_object_or_404(Post, pk = request.POST["post_id"] )
        
        liked_users = post_obj.liked_users.all()

        if self.request.user not in liked_users:
            post_obj.liked_users.add(self.request.user)

        
        activity = Activity(user =  self.request.user, action = "liked", target = post_obj  )
        activity.save()

        return redirect('post:postDetail', pk = request.POST["post_id"] )
