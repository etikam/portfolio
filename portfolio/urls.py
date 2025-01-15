from __future__ import annotations

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index
from .views import ProjectDetailView
from .views import SkillCreateView

urlpatterns = [
    path("", index, name="home"),
    path("skill/create/", SkillCreateView.as_view(), name="skill-create"),
    path("projectDetail/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
]
