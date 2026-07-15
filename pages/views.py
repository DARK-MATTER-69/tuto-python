from django.http import HttpResponse
from django.shortcuts import render

from .models import ContactMessage



def home_page_view (request):
    context = {
        'nom': 'brayann',
        'age': 20,
        'couleurs': ['noir','bleu'],
        'est_connecte': True 
    }
    return render(request, 'home.html', context)

def contact_page_view (request):
    return render(request, 'contact.html')

def message_list_view(request):
    message = ContactMessage.objects.all()
    context = {
        'message_list': message
    }
    return render(request, 'message_list.html', context)
