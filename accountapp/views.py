from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_reqired
from accountapp.forms import AccountCreationForm
from accountapp.models import Gyullos

#7/20 decorator
@login_required(login_url=reverse_lazy('accountapp:login'))
def gyullo(request):
    #7/19#로그인 되었는지 안되었는지 여부 is_auth~
    #7/20if else지우기
    if request.method == 'POST' :

        # 임시데이터 작성
        temp = request.POST.get('gyullo_input')

        new_gyullo = Gyullos()
        new_gyullo.text = temp #문제가 생기면 중단점을 잡고 확인을 해야함
        new_gyullo.save()

        gyullo_list = Gyullos.objects.all()
#post #redirect #/accounts/hello_world/
        return HttpResponseRedirect(reverse('accountapp:gyullo')) #어떤 앱 안에 있는 헬로 월드로 가라 #reverse로 redirect
#get
    else :
        gyullo_list =   Gyullos.objects.all()
        return render(request, 'accountapp/gyullo.html',
                      context={'gyullo_list': gyullo_list})

#7/12
#crud start
#create view 상속
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:gyullo')#클래스에서 리버스를 쓰기위함 why?Class와 Funtion은 불러오는 동선이 달라서 but 어카운트 앱에서 헬로월드로 가는건 같음
    template_name = 'accountapp/create.html'#create.html만드는 건 나중에

#7/15
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'#객체 접근
    template_name = 'accountapp/detail.html'

#7/20 메서드에 적용하기 위한 decorator
#메서드 데이터의 장점 - 리스트로 인자를 받을 수 있음
has_ownership = [login_required, account_ownership_reqired]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:gyullo')
    template_name = 'accountapp/update.html'

    #7/20 get에 @login_required를 쓰면 메서드기 때문에 적용 안됨

#7/20
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:gyullo')
    template_name = 'accountapp/delete.html'

