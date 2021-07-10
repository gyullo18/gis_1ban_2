
from django.urls import path

from accountapp.views import hi

app_name ='accountapp'

#'accountapp:hi'
#나중에 이런식으로 앱네임을 이용하면 편함

urlpatterns = [
    path('hi/', hi, name = 'hi' )
]