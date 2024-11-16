from django.urls import path
from .views import index, SkillCreateView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="home"),
    path("skill/create/", SkillCreateView.as_view(), name="skill-create"),
    path("projectDetail/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
