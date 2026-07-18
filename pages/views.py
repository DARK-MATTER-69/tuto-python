from .forms import ContactForm
from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from .models import ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



# def home_page_view (request):
#     context = {
#         'nom': 'brayann',
#         'age': 20,
#         'couleurs': ['noir','bleu'],
#         'est_connecte': True 
#     }
#     return render(request, 'home.html', context)


def contact_page_view (request):
    succes_msg = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            succes_msg = "formulaire sousmit avec succes"
            form = ContactForm()
    else:
        form = ContactForm() 
    context = {
        'form': form,
        'succes_msg': succes_msg
    }   
    return render(request, 'contact.html', context)


class MessageListView(ListView):
    model = ContactMessage
    template_name = "ContactMessage.html"
    context_object_name = "message_list"



# def message_list_view(request):
#     message = ContactMessage.objects.all()
#     context = {
#         'message_list': message
#     }
#     return render(request, 'message_list.html', context)
