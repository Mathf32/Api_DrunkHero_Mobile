from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Monster,Item, Utilisateur
from .serializer import MonsterSerializer,ItemSerializer,UtilisateurSerializer

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer