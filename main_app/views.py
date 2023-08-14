from django.shortcuts import render

# Create your views here.
plants = [
    {'name': 'Monstera', 'description': 'Monstera is a genus of 59 species of flowering plants in the arum family, Araceae, native to tropical regions of the Americas. Monstera plants make great indoor house plants.', 'size': 'small to very large'},
    {'name': 'Basil', 'description': 'Basil, also called great basil, is a culinary herb of the family Lamiaceae. It is a tender plant, and is used in cuisines worldwide. ', 'size': 'small to medium'},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})
