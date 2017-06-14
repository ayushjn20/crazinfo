from django.contrib import admin
from news.models import feed, UserProfile 

# Register your models here.
class feedAdmin(admin.ModelAdmin):
	fields = ['title','description','source','author','url','urlToImage','publishedAt','users']

admin.site.register(feed, feedAdmin)
	
class UP_Admin(admin.ModelAdmin):
	fields = ['dp','Bio','user', 'phoneNo']

admin.site.register(UserProfile, UP_Admin)
