from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Categorie
from .forms import Film
from .forms import Personne
from .forms import Commentaire
from .forms import Acteur
from . import models

def main(request):
	return render(request,"home.html")


def formulaire_categorie(request):
	if request.method == "POST":
		form = Categorie(request.POST)
		if form.is_valid():
			categorie = form.save()

			return HttpResponseRedirect("/categorie/main_categorie")
		else:
			form = Categorie()
			return render(request,"categorie/formulaire_categorie.html",{"form_categorie": form})
	else:
		form = Categorie()
		return render(request,"categorie/formulaire_categorie.html",{"form_categorie": form})


def traitement_categorie(request):
	form = Categorie(request.POST)
	if form.is_valid():
		categorie = form.save()
		return HttpResponseRedirect("/main-categorie/")
	else:
		categorie=Categorie
		return render(request,"categorie/formulaire_categorie.html",{"categorie": categorie})

def main_categorie(request):
	liste = list(models.categorie.objects.all())
	return render(request,"categorie/main_categorie.html",{"categories": liste})

def affiche_categorie(request, id):
	categorie = models.categorie.objects.get(pk=id)
	liste=list(models.film.objects.filter(categorie=categorie))
	return render(request,'categorie/affiche_categorie.html',{"categorie": categorie,"liste":liste})


def update_categorie(request, id):
	categorie = models.categorie.objects.get(pk=id)
	form = Categorie(categorie.dictionnaire())


	return render(request,'categorie/formulaire_categorie.html',{"form_categorie": form, "id_categorie":id})


def updatetraitement_categorie(request, id):
	form = Categorie(request.POST)
	if form.is_valid():
		categorie = form.save(commit=False)
		categorie.id = id
		categorie.save()
		return HttpResponseRedirect(f"/main-catégorie/")
	else:
		return render(request,"categorie/formulaire_categorie.html",{"form_categorie": form, "id_categorie":id})





def delete_categorie(request, id):
	categorie = models.categorie.objects.get(pk=id)
	categorie.delete()
	return HttpResponseRedirect("/categorie/main_categorie")




#.....................................................................................................................................................







def formulaire_film(request):
	if request.method == "POST":
		form = Film(request.POST)
		if form.is_valid():
			film = form.save()

			return HttpResponseRedirect("/film/main_film")
		else:
			form = Film()
			return render(request,"film/formulaire_film.html",{"form_film": form})
	else:
		form = Film()
		return render(request,"film/formulaire_film.html",{"form_film": form})


def traitement_film(request):
	form = Film(request.POST)
	if form.is_valid():
		film = form.save()
		return HttpResponseRedirect("/main-film/")
	else:
		film=Film
		return render(request,"film/formulaire_film.html",{"film": film})

def main_film(request):
	liste = list(models.film.objects.all())
	return render(request,"film/main_film.html",{"films": liste})

def affiche_film(request, id):
	film = models.film.objects.get(pk=id)
	liste3 = list(models.commentaire.objects.filter(film_id=id))
	liste=list(models.acteur.objects.filter(film=film))
	return render(request,'film/affiche_film.html',{"film": film ,"liste":liste,"liste3":liste3})


def update_film(request, id):
	film = models.film.objects.get(pk=id)
	form = Film(film.dictionnaire())
	return render(request,'film/formulaire_film.html',{"form_film": form, "id_film":id})


def updatetraitement_film(request, id):
	form = Film(request.POST)
	if form.is_valid():
		film = form.save(commit=False)
		film.id = id
		film.save()
		return HttpResponseRedirect(f"/main-film/")
	else:
		return render(request,"film/formulaire_film.html",{"form_film": form, "id_film":id})

def delete_film(request, id):
	film = models.film.objects.get(pk=id)
	film.delete()
	return HttpResponseRedirect("/film/main_film")






#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


def formulaire_acteur(request):
	if request.method == "POST":
		form = Acteur(request.POST)
		if form.is_valid():
			acteur = form.save()

			return HttpResponseRedirect("/acteur/main_acteur")
		else:
			form = Acteur()
			return render(request,"acteur/formulaire_acteur.html",{"form_acteur": form})
	else:
		form = Acteur()
		return render(request,"acteur/formulaire_acteur.html",{"form_acteur": form})


def traitement_acteur(request):
	form = Acteur(request.POST)
	if form.is_valid():
		acteur = form.save()
		return HttpResponseRedirect("/main-acteur/")
	else:
		acteur=Acteur
		return render(request,"acteur/formulaire_acteur.html",{"acteur": acteur})

def main_acteur(request):
	liste = list(models.acteur.objects.all())
	return render(request,"acteur/main_acteur.html",{"acteurs": liste})

def affiche_acteur(request, id):
	acteur = models.acteur.objects.get(pk=id)
	return render(request,'acteur/affiche_acteur.html',{"acteur": acteur})


def update_acteur(request, id):
	acteur = models.acteur.objects.get(pk=id)
	form = Acteur(acteur.dictionnaire())
	return render(request,'acteur/formulaire_acteur.html',{"form_acteur": form, "id_acteur":id})


def updatetraitement_acteur(request, id):
	form = Acteur(request.POST)
	if form.is_valid():
		acteur = form.save(commit=False)
		acteur.id = id
		acteur.save()
		return HttpResponseRedirect(f"/main-acteur/")
	else:
		return render(request,"acteur/formulaire_acteur.html",{"form_acteur": form, "id_acteur":id})

def delete_acteur(request, id):
	acteur = models.acteur.objects.get(pk=id)
	acteur.delete()
	return HttpResponseRedirect("/acteur/main_acteur")

#......................................................................................................................................................................


def formulaire_personne(request):
	if request.method == "POST":
		form = Personne(request.POST)
		if form.is_valid():
			personne = form.save()

			return HttpResponseRedirect("/personne/main_personne")
		else:
			form = Personne()
			return render(request,"personne/formulaire_personne.html",{"form_personne": form})
	else:
		form = Personne()
		return render(request,"personne/formulaire_personne.html",{"form_personne": form})


def traitement_personne(request):
	form = Personne(request.POST)
	if form.is_valid():
		personne = form.save()
		return HttpResponseRedirect("/main-personne/")
	else:
		personne=Personne
		return render(request,"personne/formulaire_personne.html",{"personne": personne})

def main_personne(request):
	liste = list(models.personne.objects.all())
	return render(request,"personne/main_personne.html",{"personnes": liste})

def affiche_personne(request, id):
	personne = models.personne.objects.get(pk=id)
	return render(request,'personne/affiche_personne.html',{"personne": personne})


def update_personne(request, id):
	personne = models.personne.objects.get(pk=id)
	form = Personne(personne.dictionnaire())
	return render(request,'personne/formulaire_personne.html',{"form_personne": form, "id_personne":id})


def updatetraitement_personne(request, id):
	form = Personne(request.POST)
	if form.is_valid():
		personne = form.save(commit=False)
		personne.id = id
		personne.save()
		return HttpResponseRedirect(f"/main-personne/")
	else:
		return render(request,"personne/formulaire_personne.html",{"form_personne": form, "id_personne":id})

def delete_personne(request, id):
	personne = models.personne.objects.get(pk=id)
	personne.delete()
	return HttpResponseRedirect("/personne/main-personne/")


#.......................................................................................................................


def formulaire_commentaire(request):
	if request.method == "POST":
		form = Commentaire(request.POST)
		if form.is_valid():
			commentaire = form.save()

			return HttpResponseRedirect("/commentaire/main_commentaire")
		else:
			form = Commentaire()
			return render(request,"commentaire/formulaire_commentaire.html",{"form_commentaire": form})
	else:
		form = Commentaire()
		return render(request,"commentaire/formulaire_commentaire.html",{"form_commentaire": form})


def traitement_commentaire(request):
	form = Commentaire(request.POST)
	if form.is_valid():
		comentaire = form.save()
		return HttpResponseRedirect("/main-commentaire/")
	else:
		commentaire=Commentaire
		return render(request,"commentaire/formulaire_commentaire.html",{"commentaire": commentaire})

def main_commentaire(request):
	liste = list(models.commentaire.objects.all())
	return render(request,"commentaire/main_commentaire.html",{"commentaires": liste})

def affiche_commentaire(request, id):
	commentaire = models.commentaire.objects.get(pk=id)
	return render(request,'commentaire/affiche_commentaire.html',{"commentaire": commentaire})


def update_commentaire(request, id):
	commentaire = models.commentaire.objects.get(pk=id)
	form = Commentaire(commentaire.dictionnaire())
	return render(request,'commentaire/formulaire_commentaire.html',{"form_commentaire": form, "id_commentaire":id})


def updatetraitement_commentaire(request, id):
	form = Acteur(request.POST)
	if form.is_valid():
		commentaire = form.save(commit=False)
		commentaire.id = id
		commentaire.save()
		return HttpResponseRedirect(f"/main-commentaire/")
	else:
		return render(request,"commentaire/formulaire_commentaire.html",{"form_commentaire": form, "id_commentaire":id})

def delete_commentaire(request, id):
	commentaire = models.commentaire.objects.get(pk=id)
	commentaire.delete()
	return HttpResponseRedirect("/commentaire/main-commentaire/")