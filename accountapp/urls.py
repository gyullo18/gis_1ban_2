
from django.urls import path

from accountapp.views import gyullo

app_name ='accountapp'

#'accountapp:hi'
#나중에 이런식으로 앱네임을 이용하면 편함

urlpatterns = [
    path('gyullo/', gyullo, name = 'hi' )
]