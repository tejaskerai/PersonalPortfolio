from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/portfolio/images/')
    tech_stack = models.TextField(default="")
    githubUrl = models.CharField(max_length=200, default="")
    url = EmbedVideoField()


    def __str__(self):
        return self.title