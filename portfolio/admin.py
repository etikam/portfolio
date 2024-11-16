from django.contrib import admin
from .models import (
    Skills,
    CategorieProject,
    ImageProject,
    Technologies,
    Projects,
    Formation,
    SoftSkill,
)

# Register your models here.


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(CategorieProject)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageProject)
class ImageProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Formation)
class AdminFormation(admin.ModelAdmin):
    pass


@admin.register(SoftSkill)
class AdminSoftSkill(admin.ModelAdmin):
    pass
