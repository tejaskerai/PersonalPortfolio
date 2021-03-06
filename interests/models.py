from django.db import models

# Create your models here.

class Interest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    moreInfo = models.BooleanField(default=False)

    def __str__(self):
        return self.title

