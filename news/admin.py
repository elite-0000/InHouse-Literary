from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'submitted')
    list_filter = ('submitted', 'date_posted')
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new object
            obj.author = request.user  # Set the author to the current user
        super().save_model(request, obj, form, change) 