from django.contrib import admin
from django.urls import path
from projetos.views import teste_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste_view, name='teste_view')
]
