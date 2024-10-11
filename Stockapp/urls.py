from django.contrib import admin
from django.urls import path
from . import views  # Assurez-vous que cela est correct

urlpatterns = [

    path('articles/ajouter/', views.create_article, name='create_article'),
    path('articles/', views.create_article, name='article_list'),  # Redirige vers le même template
    path('Tableau-De-Bord/', views.index, name='index'),  # Tableau de bord

    # URL pour enregistrer une nouvelle vente
    path('', views.create_vente, name='create_vente'),
    path('ventes/', views.vente_list, name='vente_list'),
    path('ventes/delete/<int:id>/', views.delete_vente, name='delete_vente'),
    path('livreurs/', views.livreur_list, name='livreur_list'),
    path('livreurs/supprimer/<int:id>/', views.delete_livreur, name='delete_livreur'),


]
