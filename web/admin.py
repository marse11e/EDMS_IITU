from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Document, Profile, DiscussionText


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('filename', 'status')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
    list_filter = ('approved',)
    search_fields = ('user__username', 'user__email')


@admin.register(DiscussionText)
class DiscussionTextAdmin(admin.ModelAdmin):
    list_display = ('author', 'publish_date')
    search_fields = ('author',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
