
from django.contrib import admin

from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "slug", "total_likes" )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ("created", )
    raw_id_fields = ('user',)
    ordering = ("-created",)
    search_fields = ("user", "title ")

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_user", "post", "created_time", "restricted" )
    list_filter = ("created_time", )
    raw_id_fields = ('post',)
    search_fields = ("comment_user", "post")
    ordering = ("-created_time",)

admin.site.register(Comment, CommentAdmin)