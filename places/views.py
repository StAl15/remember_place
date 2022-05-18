from django.shortcuts import render
from django.views.generic.base import View
from .models import Places


class PlacesView(View):
    def get(self, request):
        places = Places.objects.all()
        return render(request, "places/places_list.html", {"places_list": places})


class PlacesDetailView(View):
    def get(self, request, pk):
        place = Places.objects.get(id=pk)
        return render(request, "places/place_detail.html", {"place": place, "isExist": True})
