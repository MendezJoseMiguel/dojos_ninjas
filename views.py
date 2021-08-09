from django.shortcuts import render,redirect, HttpResponse
from dojo_ninja_app.models import Dojo,Ninja

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()
    context = {
        'saludo': 'Hola',
        'dojos' : dojos,
        'ninjas' : ninjas
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    desc = request.POST['desc']

    new_dojo = Dojo.objects.create(name = name,city = city, state = state, desc = desc)
    print(new_dojo)
    return redirect("/")

def create_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = Dojo.objects.get(id=int(request.POST['dojo_id']))

    new_ninja = Ninja.objects.create(first_name = first_name, last_name = last_name, dojo = dojo)
    print(new_ninja)
    return redirect("/")



