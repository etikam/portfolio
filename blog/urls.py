from __future__ import annotations

from django.urls import path

from blog.views import PostDetails
from blog.views import PostListView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("details/<int:pk>/", PostDetails.as_view(), name="blog_details"),
]
