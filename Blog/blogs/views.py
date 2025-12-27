from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """主页：所有人可见"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required # 必须登录才能访问
def new_post(request):
    """添加新帖子"""
    if request.method != 'POST':
        # 未提交数据：创建新表单
        form = BlogPostForm()
    else:
        # POST提交的数据：处理数据
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user # 自动填入当前用户
            new_post.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required # 必须登录才能访问
def edit_post(request, post_id):
    """编辑帖子"""
    post = get_object_or_404(BlogPost, id=post_id)

    # === 19-5 核心保护 ===
    # 检查帖子主人是不是当前用户
    if post.owner != request.user:
        raise Http404("你不能编辑别人的文章！")

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)