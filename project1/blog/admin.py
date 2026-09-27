from django.contrib import admin
from blog.models import Article, Comment, Tag

class TagInline(admin.StackedInline):
    model = Article.tags.through
    
class ArticleAdmin(admin.ModelAdmin):
    inline = [TagInline]

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)