from django.urls import path
from .views import (
                    index,
                    SkillCreateView
                    )


urlpatterns = [
    path('',index,name="home"),
    path('skill/create/',SkillCreateView.as_view(),name="skill-create"),
]
