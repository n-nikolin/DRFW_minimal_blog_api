from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'created', 'last_edit', 'content']
