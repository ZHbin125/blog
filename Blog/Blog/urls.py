from django.contrib import admin
from django.urls import path, include  # <--- 必须导入 include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')), 
    # 下面这行是关键！它告诉 Django：遇到空网址，去 blogs 应用里找答案
    path('', include('blogs.urls')), 
]