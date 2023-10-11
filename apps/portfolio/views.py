from django.shortcuts import render

# Create your views here.

def portfolioHomeView(request):
    return render(request, 'portfolio/portfolio.html')