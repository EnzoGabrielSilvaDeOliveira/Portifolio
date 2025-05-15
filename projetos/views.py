from django.shortcuts import render

# Create your views here.

def teste_view(request):
    return render(request, 'teste.html')

