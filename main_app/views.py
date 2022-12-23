from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dragon

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dragons_index(request):
  dragons = Dragon.objects.all()
  return render(request, 'dragons/index.html', {'dragons': dragons})

def dragons_detail(request, dragon_id):
  dragon = Dragon.objects.get(id=dragon_id)
  return render(request, 'dragons/detail.html', {'dragon': dragon})

class DragonCreate(CreateView):
    model = Dragon
    fields = '__all__'

class DragonUpdate(UpdateView):
    model = Dragon
    fields = ['color', 'description']

class DragonDelete(DeleteView):
    model = Dragon
    success_url = '/dragons/'