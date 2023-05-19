from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name

class LearningResource(models.Model):
    RESOURCE_TYPES = [
        ('B', 'Book'),
        ('V', 'Video'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    topics = models.ManyToManyField(Topic)
    location = models.URLField(max_length=200)
    resource_type = models.CharField(max_length=1, choices=RESOURCE_TYPES)
    page_count = models.IntegerField(null=True, blank=True)
    video_duration = models.DurationField(null=True, blank=True)
    progress_pages = models.IntegerField(null=True, blank=True)
    progress_time = models.DurationField(null=True, blank=True)
    progress_percent = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_resources')

    def save(self, *args, **kwargs):
        if self.resource_type == 'B' and self.page_count and self.progress_pages:
            self.progress_percent = (self.progress_pages / self.page_count) * 100
        elif self.resource_type == 'V' and self.video_duration and self.progress_time:
            self.progress_percent = (self.progress_time / self.video_duration) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
