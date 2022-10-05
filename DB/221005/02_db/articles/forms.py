from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__' # 어떤 내용을 출력할 것인가
        exclude = ('article','user',)