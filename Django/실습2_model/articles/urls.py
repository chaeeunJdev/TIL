from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # 지금 index는 주소가 없기때문에 그냥 /articles치면 들어가짐!
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
