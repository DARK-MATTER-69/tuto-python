from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


def accueil_view(request):
    return render (request, 'accueil.html')

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