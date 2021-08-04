from django.urls import path
from django.views.decorators.cache import cache_page

from . import views 


urlpatterns = [
    path ("", cache_page(60*2)(views.Home.as_view()), name="home")  ## cached this view for 2 minutes
]