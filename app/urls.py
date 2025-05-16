from django.contrib import admin
from django.urls import path
from projetos.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view(), name='home')
]
