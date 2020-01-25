from django.contrib import admin
from .models import Post

# this makes the post info more clear on the admin page
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} # slug automatically filled based on title

admin.site.register(Post, PostAdmin)

#admin.site.register(Post)
