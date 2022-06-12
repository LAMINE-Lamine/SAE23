from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),

    path('categorie/formulaire_categorie', views.formulaire_categorie),
    path('categorie/main_categorie', views.main_categorie),
    path('affiche-categorie/<int:id>/', views.affiche_categorie),
    path('delete-categorie/<int:id>/', views.delete_categorie),
    path('update-categorie/<int:id>/', views.update_categorie),
    path('updatetraitement-categorie/<int:id>/', views.updatetraitement_categorie),

    path('film/formulaire_film', views.formulaire_film),
    #path('traitement-film/', views.traitement_film),
    path('film/main_film', views.main_film),
    path('affiche-film/<int:id>/', views.affiche_film),
    path('delete-film/<int:id>/', views.delete_film),
    path('update-film/<int:id>/', views.update_film),
    path('updatetraitement-film/<int:id>/', views.updatetraitement_film),

    path('acteur/formulaire_acteur', views.formulaire_acteur),
    #path('traitement-acteur/', views.traitement_acteur),
    path('acteur/main_acteur', views.main_acteur),
    path('affiche-acteur/<int:id>/', views.affiche_acteur),
    path('delete-acteur/<int:id>/', views.delete_acteur),
    path('update-acteur/<int:id>/', views.update_acteur),
    path('updatetraitement-acteur/<int:id>/', views.updatetraitement_acteur),

    path('commentaire/formulaire_commentaire', views.formulaire_commentaire),
    path('traitement-commentaire/', views.traitement_commentaire),
    path('commentaire/main_commentaire', views.main_commentaire),
    path('affiche-commentaire/<int:id>/', views.affiche_commentaire),
    path('delete-commentaire/<int:id>/', views.delete_commentaire),
    path('update-commentaire/<int:id>/', views.update_commentaire),
    path('updatetraitement-commentaire/<int:id>/', views.updatetraitement_commentaire),

    path('personne/formulaire_personne', views.formulaire_personne),
    path('traitement-personne/', views.traitement_personne),
    path('personne/main_personne', views.main_personne),
    path('affiche-personne/<int:id>/', views.affiche_personne),
    path('delete-personne/<int:id>/', views.delete_personne),
    path('update-personne/<int:id>/', views.update_personne),
    path('updatetraitement-personne/<int:id>/', views.updatetraitement_personne),
]