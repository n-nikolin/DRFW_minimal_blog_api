from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    title= models.CharField(max_length=100, blank=False)
    content=models.JSONField()

    class Meta:
        ordering=['created']
