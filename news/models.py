from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs=FileSystemStorage(location='news/static/images/')
# Create your models here.
class feed(models.Model):
	author = models.CharField(max_length=20, null=True)
	title = models.CharField(max_length=100, null=True)
	description = models.TextField(null = True)
	url = models.URLField(max_length=200)
	urlToImage = models.URLField(max_length=200,null=True)
	publishedAt = models.DateTimeField("News published at", null=True)
	#likes = models.IntegerField(default=0)
	users = models.ManyToManyField(User, blank=True)
	source = models.CharField(max_length=20,null=True)
	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, blank=True)
	dp = models.ImageField(storage=fs , null=True , blank=True)
	phoneNo = models.CharField(max_length=12,null=True)
	Bio = models.TextField(max_length=300,null = True)
	
	#def __unicode__(self):
	#	return self.user__username

class comment(models.Model):
	key = models.ForeignKey('feed')
	user=models.ForeignKey(User, null=True, blank=True)
	comment = models.TextField()
