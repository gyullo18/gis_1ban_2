from django.urls import path
#7/26
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),#어떤 주소로 접근하는지, 로직(as view), name
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')
]
#라우팅 끝 --- > profileapp에 템플릿 디렉토리 생성 >> profile디렉토리 생성 -> html파일