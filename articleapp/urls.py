#7/29 터미널 - python managy.py startapp articleapp
#메인의 settings의 installed에 articleapp추가
#메인 urls에 경로 추가 후 articleapp에 urls파일 생성
from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html', name='list'))
]