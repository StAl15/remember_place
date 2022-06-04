from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Places
from .forms import PlaceForm


class PlacesView(View):
    def get(self, request):
        places = Places.objects.all()
        return render(request, "places/places_list.html", {"places_list": places})


class PlacesDetailView(View):
    def get(self, request, pk):
        place = Places.objects.get(id=pk)
        return render(request, "places/place_detail.html", {"place": place, "isExist": True, "id": str(place.id)})


    def post(self, request, pk):
        form = PlaceForm(request.POST)
        if form.is_valid():
            Places.objects.filter(id=pk).update(place=form.place, description=form.description)
        return redirect('/')

    def delete(self, request, pk):
        place = Places.objects.get(id=pk)
        place.delete()
        return redirect('/')


class AddPlace(View):
    def get(self, request):
        return render(request, "places/add_place.html")

    def post(self, request):
        form = PlaceForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("/")
