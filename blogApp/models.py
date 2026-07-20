from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    auteur = models.ForeignKey(
        to= User,
        on_delete=models.PROTECT,
        related_name='article_ecrit'
    )
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre