from django.shortcuts import render
from django.http import HttpResponse
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