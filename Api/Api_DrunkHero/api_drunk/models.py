from django.db import models

# Create your models here.

class Item(models.Model):
    # Définir les champs en utilisant les types Django
    dammage_min = models.IntegerField()
    dammage_max = models.IntegerField()
    armor = models.IntegerField()
    pv = models.IntegerField()
    dodgeChance = models.IntegerField()
    critChance = models.IntegerField()
    image = models.CharField(max_length=255)  # Pour une URL ou un chemin d'image

    # Optionnel: Ajouter un nom lisible pour l'instance (utile pour l'admin ou les requêtes)
    def __str__(self):
        return f"Item {self.id} - Min Damage: {self.dammage_min} Max Damage: {self.dammage_max}"

    # Optionnel: Ajouter une méthode pour l'API, comme des calculs ou des valeurs dérivées si nécessaire
    def calculate_damage(self):
        return (self.dammage_min + self.dammage_max) / 2

class Monster(models.Model):
    dammage_min = models.IntegerField()
    dammage_max = models.IntegerField()
    armor = models.IntegerField()
    pv_max = models.IntegerField()
    pv_actuel = models.IntegerField()
    dodgechance = models.IntegerField()
    critchance = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"Monster {self.id} - Min Damage: {self.dammage_min}, Max Damage: {self.dammage_max}"

class Utilisateur(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Assurez-vous que le nom d'utilisateur est unique
    email = models.EmailField(unique=True)  # Utilisez EmailField pour valider l'email
    password = models.CharField(max_length=255)  # Le mot de passe est stocké sous forme de chaîne
    lvl = models.IntegerField(default=1)  # Niveau initialisé à 1
    cash = models.IntegerField(default=0)  # L'argent initialisé à 0
    upgradebought = models.JSONField(default=list)  # Stocke une liste JSON pour les mises à jour achetées
    skinbought = models.JSONField(default=list)  # Stocke une liste JSON pour les skins achetés
    bestwave = models.IntegerField(default=0)  # Meilleure vague, initialisée à 0

    def __str__(self):
        return f"User {self.username} - Level: {self.lvl}, Cash: {self.cash}, Best Wave: {self.bestwave}"



