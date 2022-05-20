from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlacesView.as_view()),
    path("<int:pk>/", views.PlacesDetailView.as_view()),
    path("add_place/", views.AddPlace.as_view(), name="add_place")
]
