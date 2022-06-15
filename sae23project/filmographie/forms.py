from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class Categorie(ModelForm):
    class Meta:
        model = models.categorie
        fields = ('nom', 'descriptif')
        labels = {

            'nom': _('Nom'),
            'descriptif': _("Descriptif")
        }


class Film(ModelForm):
    class Meta:
        model = models.film
        fields = ('nom', 'annee_de_sortie', 'affiche', 'realisateur', 'categorie')
        labels = {
            'nom': _("Nom"),

            'annee_de_sortie': _('Annee_de_sortie'),
            'affiche': _('Affiche'),
            'realisateur': _('Realisateur'),
            'categorie': _('Categorie')
        }


class Personne(ModelForm):
    class Meta:
        model = models.personne
        fields = ('pseudo', 'nom_prenom', 'mail', 'mot_de_passe', 'type')
        labels = {

            'pseudo': _('Pseudo'),
            'nom_prenom': _('Nom_prenom'),
            'mail': _('Mail'),
            'mot_de_passe': _('Mot_de_passe'),
            'type': _('Type')
        }


class Acteur(ModelForm):
    class Meta:
        model = models.acteur
        fields = ('film','nom', 'prenom', 'age', 'photos')
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'age': _('Age'),
            'film': _('Film'),
            'photos': _('Photos')
    }


class Commentaire(ModelForm):
    class Meta:
        model = models.commentaire

        fields = ('film', 'personnes', 'note', 'commentaire', 'date')
        labels = {
            'nom': _('Nom'),
            'personnes': _('Personnes'),
            'commentaire': _('Commentaire'),
            'date': _('Date')

    }