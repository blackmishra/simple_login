from django.urls import path

# from rest_framework import routers
from posts.views import PostView

# app_name = "posts_app"
# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet, basename='api-post')

urlpatterns = [
    # path('view_all', include(router.urls)),
    path("view_all", PostView.as_view(), name="view_all"),
]
