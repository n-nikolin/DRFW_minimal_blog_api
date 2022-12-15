from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    title= models.CharField(max_length=100, blank=False)
    content=RichTextUploadingField()

    class Meta:
        ordering=['created']
