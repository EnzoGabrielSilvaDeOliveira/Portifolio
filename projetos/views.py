from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'title': 'Home',
        'description': 'Welcome to the home page of our Django application!'
    }

