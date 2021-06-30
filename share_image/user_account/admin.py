from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "date_of_birth" )
    list_filter = ("date_of_birth", )
    search_fields = ("user", "city")


admin.site.register(Profile,ProfileAdmin)
