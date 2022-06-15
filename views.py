from django.shortcuts import render
from homework.models import Home

# Create your views here.
def index(request):
    act = Home.objects.all
    active ={'act' : act,}
    return render(request, 'index.html', active)


def details(request):
    #active = homework.object.get(pk)
    return render(request, 'details.html')




