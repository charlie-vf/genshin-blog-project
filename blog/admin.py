from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Decorator to register Post model & PostAdmin class with Admin Site
# Post Admin - Allows creation & management of posts
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


# Decorator to register Comment model & CommentAdmin class with Admin Site
# Comment Admin - Allows management of comments
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    # Comments must be approved before they are posted
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
