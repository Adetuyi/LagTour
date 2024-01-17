from django.urls import path
from . import views
from .views import locationDetails, locationsList


urlpatterns = [
    path('all-locations/', locationsList),
    path('locations/<str:pk>/', locationDetails),
]
