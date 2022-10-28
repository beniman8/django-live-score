from urllib import response
from django.shortcuts import render
from .models import Fixture
def index(request):

    return render(request,'index.html')


def fixtures(request):
    fixtures = Fixture.objects.all() 

    all_complete =  all(f.game_finished for f in fixtures)
    context = {'fixtures':fixtures,'all_complete':all_complete}
    if request.htmx:
        if all_complete:
            response= render(request,'partials/fixturelist.html',context)
            response['HX-Refresh']='true'
            return response
        return render(request,'partials/fixturelist.html',context)
    return render(request,'fixtures.html',context)
