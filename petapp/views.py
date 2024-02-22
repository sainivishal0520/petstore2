from django.shortcuts import render
from .models import pet

# Create your views here.
def pets_by_breed(request):
    lab = pet.objects.get_pet_by_breed('lab')
    return render(request, 'petapp/pets_by_breed.html', {'lab': lab})
