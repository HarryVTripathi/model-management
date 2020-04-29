from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import FashionModel

def get_details(request, id):
  # fashion_model = FashionModel.objects.get(pk=id)
  fashion_model = get_object_or_404(FashionModel, pk=id)
  return render(request, "fashionmodels/details.html", {
    "fashion_model": fashion_model
  })