from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

# from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     """A viewset to show, edit, delete and update posts"""
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostView(APIView):
    def get(self, request):
        if request.session.get("user") is None:
            return redirect("login")
        posts = Post.objects.all()
        # the many param informs the serializer that it will be
        # serializing more than a single article.
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})
