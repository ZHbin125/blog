from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text'] # 用户只需要填标题和内容
        labels = {'title': '标题', 'text': '正文'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}