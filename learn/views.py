from rest_framework import viewsets
from .models import LearningResource, Topic
from .serializers import LearningResourceSerializer, TopicSerializer

class LearningResourceViewSet(viewsets.ModelViewSet):
    queryset = LearningResource.objects.all()
    serializer_class = LearningResourceSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
