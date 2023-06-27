from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """A viewset to show, edit, delete and update posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer