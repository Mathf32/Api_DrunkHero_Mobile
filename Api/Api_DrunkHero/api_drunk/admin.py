from django.contrib import admin
from .models import Utilisateur,Item,Monster

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'dammage_min', 'dammage_max', 'armor', 'pv', 'dodgeChance', 'critChance', 'image')  # Champs affichés dans la liste
    search_fields = ('image', 'dammage_min', 'dammage_max')  # Champs recherchables
    list_filter = ('armor', 'pv')  # Filtres disponibles dans l'interface d'administration
    ordering = ('id',)  # Tri par ID par défaut

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'lvl', 'cash', 'bestwave')
    search_fields = ('username', 'email', 'lvl')  # Recherchable sur des champs spécifiques
    list_filter = ('lvl', 'cash')  # Filtres disponibles
    ordering = ('id',)  # Tri par ID par défaut

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('id', 'dammage_min', 'dammage_max', 'armor', 'pv_max', 'pv_actuel', 'dodgechance', 'critchance', 'image')
    search_fields = ('id', 'dammage_min', 'dammage_max', 'image')  # Champs recherchables
    list_filter = ('armor', 'pv_max')  # Filtres dans l'interface d'administration
    ordering = ('id',)  # Tri par ID par défaut