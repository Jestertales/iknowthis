from django.db import models

# Create your models here.
class Blog(models.Model):
    titel = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel