from rest_framework import serializers
from news.models import feed

class FeedSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True)
	description = serializes.TextField(required=False, allow_blank=True)
	url = serializes.URLField()
	urlToImage =serializes.URLField(required=False, allow_blank=True)
	publishedAt = serializes.DateTimeField(required=False, allow_blank=True)
	users = serializes.ManyToManyField(required=False, allow_blank=True)
	source = serializes.CharField()
	def create(self, validated_data):
		return feed.objects.create(**validated_data)
