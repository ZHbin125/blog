from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """博客帖子表单（用于新建和编辑）"""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # 仅展示标题和正文，所有者自动关联
        labels = {
            'title': '帖子标题',
            'text': '帖子正文'
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10})  # 自定义文本框大小
        }