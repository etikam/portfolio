from django.contrib import admin
from blog.models import Article, Comment, Category

# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_active')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass