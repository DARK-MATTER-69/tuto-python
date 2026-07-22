from django import forms
from blogApp.models import Article

class ArticleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre','contenu']


