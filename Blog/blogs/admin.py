from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    """自定义Admin展示，显示帖子所属用户"""
    list_display = ['title', 'owner', 'date_added']  # 列表页显示字段
    list_filter = ['owner']  # 按用户筛选
    search_fields = ['title']  # 按标题搜索

# 注册模型和自定义Admin类
admin.site.register(BlogPost, BlogPostAdmin)