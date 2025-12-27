from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """首页：公开可见，按创建时间倒序展示所有帖子"""
    # 降序排列，最新帖子在前
    blog_posts = BlogPost.objects.all().order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """新建帖子：仅登录用户可访问，自动关联当前用户为所有者"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # 先不提交到数据库，获取表单实例
            new_post = form.save(commit=False)
            # 绑定当前登录用户为所有者
            new_post.owner = request.user
            # 提交到数据库
            new_post.save()
            return redirect('blogs:index')
    else:
        # GET请求，显示空表单
        form = BlogPostForm()

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """编辑帖子：仅登录用户可访问，且仅能编辑自己的帖子"""
    # 获取要编辑的帖子，不存在则返回404
    post = get_object_or_404(BlogPost, id=post_id)

    # 权限验证：非帖子所有者禁止访问
    if post.owner != request.user:
        return HttpResponseForbidden("错误：你没有权限编辑这篇帖子！")

    if request.method == 'POST':
        # 绑定POST数据和现有帖子实例
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        # GET请求，显示填充好现有数据的表单
        form = BlogPostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)