from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    """ A post serializer to serializer the post model"""
    class Meta:
        model = Post
        fields = "__all__"