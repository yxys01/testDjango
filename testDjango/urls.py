"""testDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstWEB import views

urlpatterns = [
    # 前一个参数：访问的地址
    # admin.site.urls 你要调用的映射到views里面的文件
    path('admin/', admin.site.urls),
    # 映射到views的index功能上
    # index是访问网页的路径：http://127.0.0.1:8000/index/ 可以访问到目标网页
    path('index/', views.index),
    # http://127.0.0.1:8000/abc 可以访问到目标网页
    # path('abc', views.index)

    path('calpage/', views.CalPage),
    # 路由部分
    path('cal', views.Cal),

    path('list', views.CalList),
    path('del', views.DelData)

]
