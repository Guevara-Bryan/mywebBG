from django.urls import path

from . import views

app_name = 'the_site'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('portfolio', views.portFolioView, name='portfolio')
]