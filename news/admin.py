from django.contrib import admin
from news.models import feed, UserProfile, comment

# Register your models here.
class feedAdmin(admin.ModelAdmin):
	list_display = ['id','title','source']
	fields = ['title','description','source','author','url','urlToImage','publishedAt','users']

admin.site.register(feed, feedAdmin)
	
class UP_Admin(admin.ModelAdmin):
	list_display = ['user','phoneNo','Bio']
	fields = ['dp','Bio','user', 'phoneNo']
admin.site.register(UserProfile, UP_Admin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['id','comment','user','key']
admin.site.register(comment,CommentAdmin)
