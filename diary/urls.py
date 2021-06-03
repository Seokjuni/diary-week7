from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('목차', 목차, name = '목차'),
    path('작성', 작성, name = '작성'),
    path('새로작성', 새로작성, name = '새로작성'),
    path('<str:id>', 상세, name = '상세'),
    path('수정/<str:id>', 수정, name = '수정'),
    path('업데이트/<str:id>', 업데이트, name = '업데이트'),
    path('삭제/<str:id>', 삭제, name = '삭제'),
]