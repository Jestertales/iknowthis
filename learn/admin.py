from django.contrib import admin

# Register your models here.

from .models import Topic, LearningResource

admin.site.register(Topic)
admin.site.register(LearningResource)