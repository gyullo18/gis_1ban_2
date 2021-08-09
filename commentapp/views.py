from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

#8/9
#인증과정 추가 -- 유저라는것을 식별하기 위해서는 로그인 되어있어야함
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    # 32~33분쯤
    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')  # creta.html에 작성한 후 돌아와서 작성
        return super().form_valid(form)

    # 위처럼 하면 article_id를 바로 할당해줄 수 있다

    # 4분정도
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
    # url 연결

# 8/9
@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})
    # url 라우팅