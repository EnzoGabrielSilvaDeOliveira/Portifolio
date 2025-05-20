from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Projeto 

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'title': 'Home',
        'description': 'Welcome to the home page of our Django application!'
    }

class ProjetosPageView(ListView):
    template_name = 'projetos.html'
    extra_context = {
        'title': 'Projetos',
        'description': 'Explore our projects and initiatives!'
    }
    model = Projeto
    context_object_name = 'projetos'
