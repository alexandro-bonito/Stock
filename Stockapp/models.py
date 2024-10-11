from django.db import models

# Create your models here.
from django.db import models

# Modèle Article
class Article(models.Model):
    mention = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, unique=True)
    prix_commercial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mention or f"Article {self.code}"

# Modèle Stock
class Stock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"Stock de {self.article.mention} : {self.quantite}"

# Modèle Dépenses
class Depenses(models.Model):
    mention = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Dépense : {self.mention} - {self.montant} FCFA"

# Modèle Livreur
class Livreur(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return f"Livreur : {self.nom} - {self.prix} FCFA"
# Modèle Vente
class Vente(models.Model):
    EXPEDITION = 'expedition'
    LIVRAISON = 'livraison'
    TYPE_CHOICES = [
        (EXPEDITION, 'Expédition'),
        (LIVRAISON, 'Livraison'),
    ]

    nom_client = models.CharField(max_length=255)
    numero_client = models.CharField(max_length=20)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=EXPEDITION)
    destination = models.CharField(max_length=255)
    livreur = models.ForeignKey('Livreur', on_delete=models.SET_NULL, null=True)  # Ajout du champ livreur
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vente à {self.nom_client} - {self.article.mention}"
