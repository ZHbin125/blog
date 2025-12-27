from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """博客帖子模型（关联用户，带权限保护）"""
    title = models.CharField(max_length=200)  # 帖子标题
    text = models.TextField()  # 帖子正文
    date_added = models.DateTimeField(auto_now_add=True)  # 自动记录创建时间
    # 外键关联内置User模型，用户删除时其帖子也删除
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示（后台显示用）"""
        return self.title[:50]