from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .forms import Categorie
from .forms import Film
from .forms import Personne
from .forms import Commentaire
from .forms import Acteur
from . import models
from fpdf import FPDF
from django.shortcuts import render
from django.http import FileResponse
import csv







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
		return HttpResponseRedirect("/categorie/main_categorie")
	else:
		return render(request,"categorie/formulaire_categorie.html",{"form_categorie": form, "id_categorie":id})





def delete_categorie(request, id):
	categorie = models.categorie.objects.get(pk=id)
	categorie.delete()
	return HttpResponseRedirect("/categorie/main_categorie")


def afficheb_acteur(request, id):
	film = models.film.objects.get(pk=id)
	liste=list(models.acteur.objects.filter(film=film))
	return render(request,'categorie/afficheb_acteur.html',{"film": film,"liste":liste})




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

	liste_note=[]
	somme = 0
	max_value= 0
	min_value = 0
	if len(liste3) != 0:
		for commentaire in liste3:
			somme = somme + commentaire.note
			liste_note.append(commentaire.note)
			print('Maximum_value',max_value)
			max_value = max(liste_note)
			print('Minimum_value', min_value)
			min_value = min(liste_note)
		somme = somme / len(liste3)
		print(somme)
		print(max_value)
		print(min_value)






	return render(request,'film/affiche_film.html',{"film": film ,"liste":liste,"liste3":liste3,"somme":somme,'Maximum_value':max_value})




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
		return HttpResponseRedirect("/film/main_film")
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
	return render(request,'acteur/afficheb_acteur.html',{"acteur": acteur})


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
		return HttpResponseRedirect("/acteur/main_acteur")
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
	form = Commentaire(request.POST)
	if form.is_valid():
		commentaire = form.save(commit=False)
		commentaire.id = id
		commentaire.save()
		return HttpResponseRedirect("/commentaire/main_commentaire")
	else:
		return render(request,"commentaire/formulaire_commentaire.html",{"form_commentaire": form, "id_commentaire":id})

def delete_commentaire(request, id):
	commentaire = models.commentaire.objects.get(pk=id)
	commentaire.delete()
	return HttpResponseRedirect("/commentaire/main_commentaire")


def filmographie_pdf(request ,id):
	commentaire = models.commentaire.objects.get(pk=id)
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('Arial', size=16)
	pdf.cell(200, 10, txt="Voici les éléments des commentaires :", ln=2, align='C')
	pdf.cell(200, 10, txt="Nom du film " + str(commentaire.film), ln=2, align='C')
	pdf.cell(200, 10, txt="Le commentaire du film " + str(commentaire.commentaire), ln=2, align='C')
	pdf.cell(200, 10, txt="La note du film " + str(commentaire.note), ln=2, align='C')
	pdf.cell(200, 10, txt="La personne qui la publier " + str(commentaire.personnes), ln=2, align='C')

	pdf.cell(200, 10, txt="La date du commentaire " + str(commentaire.date), ln=2, align='C')

	pdf.output('filmographie.pdf')
	response = FileResponse(open("filmographie.pdf"))
	return response


def filmographie_csv(request,id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Dispostion'] = 'attachment; filename=filmographie_csv.csv'

    writer = csv.writer(response)
#CSV
    commentaire = models.commentaire.objects.all()

    writer.writerow(['Nom film','commentaire film ',' nom de la personne ','note du commentaire','Date commentaire'])

    for commentaire in commentaire:
        writer.writerow([commentaire.film,'      /       '      ,commentaire.commentaire,'      /       ' ,commentaire.personnes,'      /       ' ,commentaire.note,'      /       ' ,commentaire.date])

    return response