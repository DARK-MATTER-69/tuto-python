from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from blogApp.models import Article
from blogApp.froms import ArticleForm


def accueil_view(request):
    article = Article.objects.all().order_by('-date_de_creation')
    context ={
        'articles':article
    }
    return render (request, 'accueil.html', context)

def connect_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blogapp:accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form':form})

def inscription_view(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('blogapp:accueil')
    else:
        forms = UserCreationForm()
    return render(request, 'inscription.html', {'form': forms})

def deconnect_view(request):
    logout(request)
    return redirect(request, 'blogapp:accueil.html')

@login_required
def creer_un_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)  # commit permet de faire mettre en pause l'enregistrement de la requete
            new_article.auteur = request.user # donne le nom de l'auteur qui veut creer l'article 
            new_article.save()
            return redirect('blogapp:accueil')
    else :
        form = ArticleForm()
    return render (request, 'creer_form.html', {'form': form, 'action': 'Creer'})

def DetailArticleView (request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'detail_article.html', context)

@login_required
def ModificationArticleView (request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if article.auteur != request.user:
        return redirect('blogapp:detail_article', pk=article.pk)
    
    if request.method == 'POST':
        form = ArticleForm(request, instance=article)
        if form.is_valid():
            form.save()
            return redirect ('blogapp:detail_article', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context ={
        'form': form,
        'action' : 'modifier',
        'article' : article
    }
    return render (request, 'creer_form.html' ,context)
    
@login_required
def Supprimer_view (request, pk):
    article = get_object_or_404(Article, pk=pk)
        
    if article.auteur != request.user:
        return redirect('blogapp:detail_article', pk=article.pk)
    
    if request.method == 'POST':
       article.delete()
       return redirect('blogapp:accueil')

    context = {
        'article': article
    }
       
    return render (request, 'confirm_supp.html', context)