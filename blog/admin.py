from django.contrib import admin
from blog.models import Auteur, Article, Profile, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "est_publier", "nb_vue", "date_publication")
    list_filter = ("est_publier", "date_publication")
    search_fields = ("titre", "contenu")

admin.site.register(Auteur)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile)
admin.site.register(Tag)
