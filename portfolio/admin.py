from django.contrib import admin
from .models import Skills
# Register your models here.

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    pass