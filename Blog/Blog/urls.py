from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 包含blogs app的URL配置
    path('', include('blogs.urls')),
    # 内置登录视图
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # 内置退出视图
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]