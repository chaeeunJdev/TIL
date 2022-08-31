# admin 은 뺐음!
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    # 화면 추가 path("경로", 해당 경로를 처리해줄 views.py의 함수 이름)
    path("index/", views.index, name = "index"),
    path("greeting/", views.greeting, name = "greeting"),
    path("dinner/", views.dinner, name = "dinner"),
    path("throw/", views.throw, name = "throw"),
    path("catch/", views.catch, name = "catch"),
    path("hello/<name>", views.hello, name = "hello"),
]

