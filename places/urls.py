from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.PlacesView.as_view()),
    path("<int:pk>", views.PlacesDetailView.as_view(), name="place_detail"),
    path("<int:pk>/update", views.PlacesDetailView.as_view(), name="place_update"),
    path("<int:pk>/delete", views.PlacesDetailView.as_view(), name="place_delete"),
    path("add_place", views.AddPlace.as_view(), name="add_place"),

]
