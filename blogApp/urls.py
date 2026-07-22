from django.urls import path
from blogApp import views
name_app = 'blogapp'

urlpatterns = [
    path('',views.accueil_view, name='accueil'),
    path('connexion/',views.connect_view, name='connexion'),
    path('deconnexion/',views.deconnect_view, name='deconnexion'),
    path('inscription/',views.inscription_view, name='inscription'),
    path('article/creer/',views.creer_un_article, name='creer_article'),
    path('article/<int:pk>/',views.DetailArticleView, name='detail'),
    path('article/<int:pk>/modifier/',views.ModificationArticleView, name='modifier'),
    path('article/<int:pk>/supprimer/',views.ModificationArticleView, name='supprimer')
]
