from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = models.Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


# Register your models here.
admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment)
