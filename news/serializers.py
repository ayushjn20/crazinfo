from rest_framework import serializers
from news.models import feed, UserProfile, comment, reply
from django.contrib.auth.models import User
'''
class FeedSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True)
	description = serializers.CharField(required=False, allow_blank=True)
	url = serializers.URLField()
	urlToImage =serializers.URLField(required=False, allow_blank=True)
	publishedAt = serializers.DateTimeField(required=False)
	users = serializers.ManyToManyField(required=False, allow_blank=True)
	source = serializers.CharField()
	def create(self, validated_data):
		return feed.objects.create(**validated_data)
'''

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('dp',)

class UserSerializer_comments(serializers.ModelSerializer):
	#dp = UserProfileSerializer(read_only = True)
	class Meta:
		model = User
		fields = ('username',)

class FeedSerializer

class FeedSerializer(serializers.ModelSerializer):
	users = UserSerializer(read_only=True, many=True)
	class Meta:
		model = feed
		fields = ('id','title','description','url','urlToImage','publishedAt','users','source')
class CommentSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = comment
		fields = ('user','comment','key')
class ReplySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = comment
		fields = ('user','reply','key')
