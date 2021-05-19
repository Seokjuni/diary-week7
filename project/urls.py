"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from diary.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 커버, name = '커버' ),
    path('목차', 목차, name = '목차'),
    path('작성', 작성, name = '작성'),
    path('새로작성', 새로작성, name = '새로작성'),
    path('<str:id>', 상세, name = '상세'),
    path('수정/<str:id>', 수정, name = '수정'),
    path('업데이트/<str:id>', 업데이트, name = '업데이트'),
    path('삭제/<str:id>', 삭제, name = '삭제'),
]
