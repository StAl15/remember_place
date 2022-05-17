from django.shortcuts import render
from django.views.generic.base import View
from .models import Places


class PlacesView(View):
    def get(self, request):
        places = Places.place
        return render(request, "places/places_list.html", {"places_list": places})
