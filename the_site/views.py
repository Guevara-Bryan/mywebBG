from django.shortcuts import render

from .models import Project, navItem
# Create your views here.

def homeView(request):
    context = {
        'title': 'Home',
        'menu_list': navItem.objects.all()
    }
    return render(request, 'the_site/home.html',context)

def portFolioView(request):
    context = {
        'title': 'Portfolio',
        'menu_list': navItem.objects.all(),
        'projects_list': Project.objects.all()
    }
    return render(request, 'the_site/portfolio.html', context)