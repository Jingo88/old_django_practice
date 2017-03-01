from django.contrib import admin

# Register your models here.
from posts.models import Post

# check out docs for Models options
# https://docs.djangoproject.com/en/1.9/ref/models/fields/

# create a class that will be a model for Posts in the Admin page
class PostModelAdmin(admin.ModelAdmin):
	# displays other factors of the model
	list_display = ["title", "updated", "timestamp"]
	# choose which items are clickable/links
	list_display_links = ["updated"]
	# choose what parts of the list the user can edit by clicking
	list_editable = ["title"]
	# gives a default filtering box on the side
	list_filter = ["updated", "timestamp"]
	# allow us to search for specific things
	search_fields = ["title", "content"]
	
	# Connects this class to the Post model
	class Meta:
		model = Post

# added the PostModelAdmin to the admin.site.register
admin.site.register(Post, PostModelAdmin)