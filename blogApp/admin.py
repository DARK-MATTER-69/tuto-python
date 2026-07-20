from django.contrib import admin
from blogApp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_de_creation')
    list_filter = ('date_de_creation')
    search_fields = ('titre','contenu')
    
admin.site.register(Article, ArticleAdmin)
    

