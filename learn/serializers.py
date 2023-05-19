from rest_framework import serializers
from .models import Topic, LearningResource
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TopicSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'created_by']

class LearningResourceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = LearningResource
        fields = ['id', 'title', 'author', 'publication_year', 'topics', 'location', 'resource_type', 'page_count', 'video_duration', 'progress_pages', 'progress_time', 'progress_percent', 'created_by']
