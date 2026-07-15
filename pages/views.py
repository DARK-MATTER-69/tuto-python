from django.http import HttpResponse
from django.shortcuts import render



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
