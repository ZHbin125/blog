from django.urls import path
from . import views

app_name = 'blogs'  # 命名空间，避免URL冲突
urlpatterns = [
    # 首页：显示所有帖子
    path('', views.index, name='index'),
    # 新建帖子
    path('new_post/', views.new_post, name='new_post'),
    # 编辑帖子（通过post_id定位）
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]