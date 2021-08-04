from django.contrib import admin

from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "target", "created" )
    list_filter = ("created", )
    search_fields = ("action",)

admin.site.register(Activity,ActivityAdmin)


