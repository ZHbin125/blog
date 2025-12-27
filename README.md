# Django 受保护博客系统 📝

一个基于 Django 构建的安全易用博客应用，集成用户认证、帖子管理和基于角色的访问控制功能。项目支持公开浏览博客帖子，同时限制仅注册用户可创建/编辑帖子——且用户仅能修改自己发布的内容，保障数据安全。

## 🌟 核心功能

### 基础功能
- **公开访问**：未注册用户可浏览所有博客帖子，查看作者、发布时间等信息。
- **用户认证**：基于 Django 内置认证框架，支持用户登录/退出，登录后自动跳转至博客首页。
- **帖子管理**：
  - 注册用户可创建含标题和正文的博客帖子。
  - 权限隔离：用户仅能编辑自己发布的帖子，无法操作他人内容。
- **权限拦截**：
  - 尝试编辑他人帖子将返回 403 禁止访问错误。
  - 未登录用户访问创建/编辑页面时，自动重定向至登录页。
- **后台管理**：利用 Django 内置 admin 界面，可便捷管理用户、帖子数据，支持筛选和搜索。

### 技术亮点
- 遵循 Django MTV（模型-模板-视图）架构设计。
- 采用 Django ORM 处理数据库交互（默认使用 SQLite，可无缝切换至 PostgreSQL/MySQL）。
- 内置表单验证和 CSRF 防护，保障接口安全。
- 简洁响应式 UI，样式可灵活自定义。
- 完整数据持久化：帖子数据存储于数据库，重启服务器后不丢失。

## 📋 目录
- [前置要求](#前置要求)
- [安装部署](#安装部署)
- [项目结构](#项目结构)
- [使用说明](#使用说明)
- [功能详情](#功能详情)
- [配置说明](#配置说明)
- [常见问题](#常见问题)
- [未来扩展](#未来扩展)
- [许可证](#许可证)

## 🛠 前置要求

开始前请确保安装以下环境：
- Python 3.8+（推荐 3.10+ 版本）
- pip（Python 包管理工具）
- Git（用于克隆仓库）

## 🚀 安装部署

### 1. 克隆仓库
```bash
git clone https://github.com/你的用户名/django-protected-blog.git
cd django-protected-blog
```

### 2. 创建虚拟环境（可选但推荐）
```bash
# Windows 系统
python -m venv venv
venv\Scripts\activate

# macOS/Linux 系统
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
# 若未创建 requirements.txt，先执行以下命令生成
pip freeze > requirements.txt

# 安装依赖包
pip install -r requirements.txt
```

### 4. 数据库配置
```bash
# 生成迁移文件（根据模型创建数据表结构）
python manage.py makemigrations

# 执行迁移，创建数据库表
python manage.py migrate
```

### 5. 创建超级用户（用于访问 admin 后台）
```bash
python manage.py createsuperuser
```
按照提示输入用户名、邮箱（可选）和密码（需至少 8 字符，记牢密码）。

### 6. 启动开发服务器
```bash
python manage.py runserver
```
若 8000 端口被占用，可指定其他端口：
```bash
python manage.py runserver 8001  # 使用 8001 端口
```

### 7. 访问应用
打开浏览器，访问以下地址：
- **博客首页**：`http://127.0.0.1:8000/`（公开访问，可浏览所有帖子）
- **登录页**：`http://127.0.0.1:8000/login/`（使用注册用户/超级用户登录）
- **Admin 后台**：`http://127.0.0.1:8000/admin/`（使用超级用户登录，管理用户和帖子）

## 📂 项目结构

```
django-protected-blog/
├── Blog/                  # 项目配置目录
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # 项目核心配置（app注册、模板目录、认证设置等）
│   ├── urls.py            # 项目级URL路由（关联admin、登录/退出、blogs模块）
│   └── wsgi.py
├── blogs/                 # 博客功能核心模块
│   ├── __init__.py
│   ├── admin.py           # admin后台配置（帖子/用户管理）
│   ├── apps.py            # 模块配置
│   ├── forms.py           # 表单定义（新建/编辑帖子）
│   ├── migrations/        # 数据库迁移文件（自动生成）
│   ├── models.py          # 数据模型（BlogPost帖子模型）
│   ├── templates/         # 模块模板
│   │   └── blogs/
│   │       ├── index.html # 首页模板
│   │       ├── new_post.html # 新建帖子模板
│   │       └── edit_post.html # 编辑帖子模板
│   ├── tests.py           # 测试文件（可扩展）
│   ├── urls.py            # 模块级URL路由（首页、新建、编辑接口）
│   └── views.py           # 视图函数（业务逻辑处理、权限控制）
├── templates/             # 项目全局模板
│   └── registration/
│       └── login.html     # 登录页面模板
├── db.sqlite3             # 内置SQLite数据库（自动生成）
├── manage.py              # Django项目管理脚本
└── requirements.txt       # 依赖包列表
```

## 📖 使用说明

### 1. 未登录状态
- 访问首页可浏览所有帖子，查看作者、发布时间和正文。
- 无法看到「新建帖子」按钮，点击他人帖子的编辑链接会跳转至登录页。

### 2. 登录状态
- 登录后首页显示「当前用户名+退出登录+新建帖子」链接。
- 点击「新建帖子」：填写标题和正文，提交后自动保存至数据库，返回首页可见新帖子。
- 编辑帖子：仅能看到自己发布的帖子旁的「编辑」按钮，点击可修改内容并保存。

### 3. Admin 后台操作
- 登录 `http://127.0.0.1:8000/admin/`，可管理：
  - 用户：创建、修改、删除普通用户。
  - 帖子：查看所有用户的帖子，按作者筛选、按标题搜索，支持新增/编辑/删除帖子。

## 📌 功能详情

| 功能场景                | 操作路径                                  | 权限要求               |
|-------------------------|-------------------------------------------|------------------------|
| 浏览所有帖子            | 首页 `http://127.0.0.1:8000/`             | 无（公开访问）         |
| 用户登录                | 登录页 `http://127.0.0.1:8000/login/`      | 无（需输入合法账号密码）|
| 新建帖子                | 首页→「新建帖子」按钮                      | 已登录用户             |
| 编辑自有帖子            | 帖子旁「编辑」按钮→修改内容→保存           | 帖子所有者（已登录）   |
| 访问他人帖子编辑页      | 直接输入 `edit_post/<post_id>/` 路由       | 禁止（返回403错误）    |
| 管理用户/帖子           | Admin后台 `http://127.0.0.1:8000/admin/`   | 超级用户               |

## ⚙️ 配置说明

核心配置文件：`Blog/settings.py`
- **App 注册**：`INSTALLED_APPS` 中已添加 `'blogs'`，确保模块生效。
- **模板目录**：`DIRS: [os.path.join(BASE_DIR, 'templates')]`，指定全局模板路径。
- **认证配置**：
  - `LOGIN_URL = 'login'`：未登录用户访问受保护页面时，重定向至登录页。
  - `LOGIN_REDIRECT_URL = 'blogs:index'`：登录成功后跳转至博客首页。
  - `LOGOUT_REDIRECT_URL = 'blogs:index'`：退出登录后返回首页。
- **语言与时区**：默认配置为中文简体和上海时区：
  ```python
  LANGUAGE_CODE = 'zh-hans'
  TIME_ZONE = 'Asia/Shanghai'
  ```

## 🚨 常见问题

### 1. 「找不到 manage.py」错误
- 原因：终端未进入项目根目录（需进入包含 `manage.py` 的文件夹）。
- 解决：使用 `cd` 命令导航至克隆后的 `django-protected-blog` 目录。

### 2. 「拒绝连接」（ERR_CONNECTION_REFUSED）
- 原因：开发服务器未启动，或端口被占用。
- 解决：
  - 执行 `python manage.py runserver` 启动服务器。
  - 端口占用时，指定其他端口：`python manage.py runserver 8001`。

### 3. 模板加载失败（TemplateDoesNotExist）
- 原因：模板文件存放路径错误。
- 解决：确保模板文件符合以下结构：
  - 模块模板：`blogs/templates/blogs/xxx.html`
  - 登录模板：`templates/registration/login.html`

### 4. 权限控制失效（可编辑他人帖子）
- 原因：视图函数中未验证帖子所有者与当前用户的一致性。
- 解决：检查 `blogs/views.py` 中 `edit_post` 函数，确保包含以下代码：
  ```python
  if post.owner != request.user:
      return HttpResponseForbidden("你没有权限编辑这篇帖子！")
  ```

### 5. 数据库迁移失败
- 原因：模型修改后未重新生成迁移文件，或迁移记录冲突。
- 解决：
  ```bash
  # 重新生成迁移文件（谨慎使用，会覆盖现有迁移）
  python manage.py makemigrations --empty blogs
  # 重新执行迁移
  python manage.py migrate
  ```

## 🔭 未来扩展

可基于该项目扩展以下功能：
1. 帖子分类与标签：添加分类模型，支持按分类筛选帖子。
2. 评论功能：允许用户对帖子发表评论，支持评论管理。
3. 富文本编辑：集成 TinyMCE 等富文本编辑器，支持图片、格式排版。
4. 用户注册功能：添加前台注册页面，无需通过 admin 后台创建用户。
5. 帖子删除功能：允许用户删除自己的帖子。
6. 数据分页：当帖子数量较多时，实现分页展示。

## 📄 许可证

本项目基于 MIT 许可证开源，允许自由使用、修改和分发，详情见 `LICENSE` 文件。

---

欢迎 Star 🌟 本仓库，若有问题或建议，可通过 Issues 提交反馈！
