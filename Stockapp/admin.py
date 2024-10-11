from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Stock, Depenses, Livreur, Vente

# Configuration de l'admin pour le modèle Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('mention', 'code', 'prix_commercial', 'date_ajout')
    search_fields = ('mention', 'code')
    list_filter = ('date_ajout',)

# Configuration de l'admin pour le modèle Stock
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('article', 'quantite')
    search_fields = ('article__mention',)
    list_filter = ('article',)

# Configuration de l'admin pour le modèle Depenses
@admin.register(Depenses)
class DepensesAdmin(admin.ModelAdmin):
    list_display = ('mention', 'montant')
    search_fields = ('mention',)
    list_filter = ('montant',)

# Configuration de l'admin pour le modèle Livreur
@admin.register(Livreur)
class LivreurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)
    list_filter = ('prix',)

# Configuration de l'admin pour le modèle Vente
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'numero_client', 'article', 'type', 'destination', 'date')
    search_fields = ('nom_client', 'numero_client', 'article__mention', 'destination')
    list_filter = ('type', 'date')
