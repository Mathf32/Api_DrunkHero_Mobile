from rest_framework import serializers
from .models import Monster,Item,Utilisateur

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ['id', 'dammage_min', 'dammage_max', 'armor', 'pv_max', 'pv_actuel', 'dodgechance', 'critchance', 'image']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'dammage_min', 'dammage_max', 'armor', 'pv', 'dodgeChance', 'critChance', 'image']

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'password', 'lvl', 'cash', 'upgradebought', 'skinbought', 'bestwave']
        extra_kwargs = {
            'password': {'write_only': True},  # Assurez-vous que le mot de passe est uniquement en écriture
        }