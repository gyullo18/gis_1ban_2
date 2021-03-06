#7/29 터미널 - python managy.py startapp articleapp
#메인의 settings의 installed에 articleapp추가
#메인 urls에 경로 추가 후 articleapp에 urls파일 생성
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    #8/5 TemplateView.as_view(template_name='articleapp/list.html') 대신에 넣어줌
    path('list/', ArticleListView.as_view(), name='list'),
    #8/2 하고 create.html로
    path('create/', ArticleCreateView.as_view(), name='create'),
    #라우팅하고 detail.html
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    #8/4 라우팅 후 update.html
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
#8/4 라우팅 후 delete.html
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]