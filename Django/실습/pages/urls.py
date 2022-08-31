from django.urls import path
from . import views

# 빈 리스트 생성 ==> 아직 매칭할 페이지가 없다
app_name = "pages"
urlpatterns = [
    path("index/", views.index, name = "index"),
]

