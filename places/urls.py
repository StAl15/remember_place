from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path("", views.PlacesView.as_view()),
    path("<int:pk>", views.PlacesDetailView.as_view(), name="place_detail"),
    re_path(r"^places/<int:pk>/update", views.PlacesDetailView.as_view(), name="place_update"),
    re_path(r"^places/<int:pk>/delete", views.PlacesDetailView.as_view(), name="place_delete"),
    re_path(r"^add_place", views.AddPlace.as_view(), name="add_place"),

]
