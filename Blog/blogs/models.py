from django.db import models
from django.contrib.auth.models import User  # 1. 引入用户模型

class BlogPost(models.Model):
    """一篇博客文章"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 2. 关联用户 (19-5 要求：每篇文章必须属于一个人)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title