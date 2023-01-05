from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dragon, Toy
from .forms import FeedingForm

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
  toys_dragon_doesnt_have = Toy.objects.exclude(id__in = dragon.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dragons/detail.html', {
    'dragon': dragon,
    'feeding_form': feeding_form,
    'toys': toys_dragon_doesnt_have
    })

def add_feeding(request, dragon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dragon_id = dragon_id
        new_feeding.save()
    return redirect('detail', dragon_id=dragon_id)

class DragonCreate(CreateView):
    model = Dragon
    fields = '__all__'

class DragonUpdate(UpdateView):
    model = Dragon
    fields = ['color', 'description']

class DragonDelete(DeleteView):
    model = Dragon
    success_url = '/dragons/'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, dragon_id, toy_id):
  Dragon.objects.get(id=dragon_id).toys.add(toy_id)
  return redirect('detail', dragon_id=dragon_id)
