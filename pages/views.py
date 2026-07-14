from django.http import HttpResponse
from django.shortcuts import render



def home_page_view (request):
    return HttpResponse("bonjour les gens de ce monde ")
