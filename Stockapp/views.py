from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article, Vente


# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html')




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article, Vente, Livreur

# Vue pour enregistrer une vente
def create_vente(request):
    if request.method == 'POST':
        nom_client = request.POST.get('nom_client')
        numero_client = request.POST.get('numero_client')
        article_id = request.POST.get('article')
        type = request.POST.get('type')
        destination = request.POST.get('destination')
        livreur_id = request.POST.get('livreur')

        article = get_object_or_404(Article, id=article_id)
        livreur = get_object_or_404(Livreur, id=livreur_id) if livreur_id else None
        
        vente = Vente(
            nom_client=nom_client,
            numero_client=numero_client,
            article=article,
            type=type,
            destination=destination,
            livreur=livreur  # Associe le livreur à la vente
        )
        vente.save()
        
        # Message de succès
        messages.success(request, 'La Commande a été enregistrée avec succès !')
        
        return redirect('create_vente')

    articles = Article.objects.all()
    livreurs = Livreur.objects.all()  # Récupère la liste des livreurs
    return render(request, 'create_vente.html', {'articles': articles, 'livreurs': livreurs})




from django.shortcuts import render, redirect
from .models import Article

# Vue pour afficher et ajouter des articles
def create_article(request):
    if request.method == 'POST':
        mention = request.POST.get('mention')
        description = request.POST.get('description')
        code = request.POST.get('code')
        prix_commercial = request.POST.get('prix_commercial')

        article = Article(
            mention=mention, 
            description=description, 
            code=code, 
            prix_commercial=prix_commercial
        )
        article.save()
        return redirect('create_article')  # Redirige après l'ajout

    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, 'article_list.html', {'articles': articles})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Vente, Livreur

def vente_list(request):
    ventes = Vente.objects.all()
    livreurs = Livreur.objects.all()  # Récupérer tous les livreurs pour les options
    return render(request, 'vente_list.html', {'ventes': ventes, 'livreurs': livreurs})

def delete_vente(request, id):
    vente = get_object_or_404(Vente, id=id)
    vente.delete()
    return redirect('vente_list')  # Rediriger vers la liste des ventes



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livreur

# Vue pour afficher et ajouter des livreurs
def livreur_list(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prix = request.POST.get('prix')
        whatsapp = request.POST.get('whatsapp')

        # Créer et enregistrer un nouveau livreur
        livreur = Livreur(nom=nom, prix=prix, whatsapp=whatsapp)
        livreur.save()
        return redirect('livreur_list')

    # Récupérer tous les livreurs pour les afficher
    livreurs = Livreur.objects.all()
    return render(request, 'livreur_list.html', {'livreurs': livreurs})

# Vue pour supprimer un livreur
def delete_livreur(request, id):
    livreur = get_object_or_404(Livreur, id=id)
    livreur.delete()
    return redirect('livreur_list')
