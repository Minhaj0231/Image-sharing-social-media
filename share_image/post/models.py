from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

from taggit.managers import TaggableManager

from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name="user_posts")
    title = models.CharField(max_length=50, default="")
    slug = models.SlugField(default="", null=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()  
    post_image = models.ImageField(upload_to = "post_images")
    liked_users = models.ManyToManyField(User,related_name='liked_users', blank=True )
    total_likes = models.IntegerField(default=0)

    class Meta: 
        ordering = ('-created',)

    def save(self, *args, **kwargs ):

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):

        return self.title   


    def get_absolute_url(self):
        return reverse('post:postDetail', args=[self.id])


class Comment(models.Model):

    post = models.ForeignKey(Post,null=True, on_delete=models.SET_NULL, related_name="comments")
    comment_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="user_comment")
    comment_body = models.CharField(max_length=100, default="")
    created_time = models.DateTimeField(auto_now_add=True)
    restricted = models.BooleanField(default=False)    ## Admin can restrict controversial comment by this feild.


    class Meta: 
        ordering = ('-created_time',)


    def __str__(self):

        return  str(self.post)   