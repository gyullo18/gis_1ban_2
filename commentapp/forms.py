from django.forms import ModelForm

from commentapp.models import Comment

#8/5 만든후 migration까지
class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']