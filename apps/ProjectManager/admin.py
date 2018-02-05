from django.contrib import admin

# Register your models here.
from ProjectManager.models import InceptionHostConfig


@admin.register(InceptionHostConfig)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'password', 'host', 'port', 'comment')
    list_display_links = ('user',)
    search_fields = ('user',)
    ordering = ('id', )
