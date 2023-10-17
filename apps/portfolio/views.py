from django.shortcuts import render
from apps.portfolio.controllers.controller import DataController

# Create your views here.

def portfolioHomeView(request):

    projects = DataController.get_all_projects()

    context = {
        'projects': projects
    }

    print(context)

    return render(request, 'portfolio/portfolio.html', context)