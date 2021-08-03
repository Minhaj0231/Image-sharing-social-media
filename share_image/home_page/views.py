from django.shortcuts import render
from django.views.generic import ListView 
from post.models import Post
from django.contrib.auth.models import User



class Home(ListView):
    template_name = "home_page/home.html"
    model = Post
    context_object_name = "home_data"
    paginate_by = 3

    def get_queryset(self):
        base_query =  super().get_queryset()

        if self.request.user.is_authenticated:
            data =  base_query.exclude(user=self.request.user.pk)

            
            return data 



        return base_query
# def home(request):
#     # return render(request,"home_page/test.html")

    

#     return render(request, "home_page/home.html")