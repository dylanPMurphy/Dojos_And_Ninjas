from django.shortcuts import render, redirect
from dojo_ninjas_app.models import *

# Create your views here.
def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def createDojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def createNinja(request):
    dojo_id = request.POST['my_dojo']
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        my_dojo = Dojo.objects.get(id=dojo_id)
    )
    return redirect('/')