from rest_framework import viewsets
from blog.serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created')
    serializer_class = PostSerializer