from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Plant, Pot
from .forms import WateringForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    id_list = plant.pots.all().values_list('id')
    pots_plant_doesnt_have = Pot.objects.exclude(id__in=id_list)
    return render(request, 'plants/detail.html', {'plant': plant, 'watering_form': watering_form, 'pots': pots_plant_doesnt_have})


class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'


class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'


class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'


def add_watering(request, plant_id):
    # create a ModelForm instance using the data in request.POST
    form = WateringForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the plant_id assigned
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)


def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)


def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)


class PotCreate(CreateView):
    model = Pot
    fields = '__all__'
    success_url = '/pots'


class PotsList(ListView):
    model = Pot


class PotDetail(DetailView):
    model = Pot


class PotDelete(DeleteView):
    model = Pot
    success_url = "/pots"


class PotUpdate(UpdateView):
    model = Pot
    fields = '__all__'
