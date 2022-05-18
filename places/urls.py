from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlacesView.as_view()),
    path("<int:pk>/", views.PlacesDetailView.as_view())
]
