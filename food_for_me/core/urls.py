from django.urls import path
from .views import aPage
from . import views

urlpatterns = [
    path('', aPage),
    #urls para la app movil
    path('app/propaganda/',views.PropagandaListView), #List de todas las propagandas
    path('app/pymes/',views.PymeListView), #List de todas las pymes
]