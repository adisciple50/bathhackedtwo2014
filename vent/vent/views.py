from django.shortcuts import render
# import portfoilo.models as DBTables
from portfoilo.models import PortfolioExample, Contributer

def index(request):
    ListOfPortfolioArticles = PortfolioExample.objects.all()
    Context = {'PortfolioArticles': ListOfPortfolioArticles}
    return render(request,'index.html', Context)
def contributers(request):
    pass