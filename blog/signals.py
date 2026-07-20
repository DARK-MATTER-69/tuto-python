from django.db.models.signals import post_save,post_delete
from blog.models import Article
from django.dispatch import receiver


#notion de signals
#ajouter un objet
@receiver(post_save, sender=Article)
def mon_recepteur (sender, instance, created, **kwargs):
    if created:
        print (f"\n nouvelle article {instance.titre} creer ")
    else:
        print (f"\n article {instance.titre} modifier ")
        
#supprimer un objet
@receiver(post_delete, sender=Article)
def mon_recepteur_delete (sender, instance, **kwargs):
    print (f"\n  article {instance.titre} supprimer")
    
        