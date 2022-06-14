from django.db import models


class categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null=True, blank=True)



    #def __str__(self):
        #chaine = f" {self.nom} | {self.descriptif}"
       # return chaine

    def dictionnaire(self):
        return {"nom": self.nom, "description": self.descriptif, }


class film(models.Model):
    categorie = models.ManyToManyField(categorie)
    nom=models.CharField(max_length=100)
    annee_de_sortie = models.DateField()
    affiche = models.ImageField(upload_to='', storage=None, null=True, blank=True, default="APLU")
    realisateur = models.CharField(max_length=100)


    def __str__(self):
        str = "categories: "
        for i in list(self.categorie.all()):
            str = str + i.nom + " , "


        chaine = f"{self.nom} "
        return chaine

    def dictionnaire(self):
        return {"nom": self.nom , "annee_de_sortie": self.annee_de_sortie, "affiche": self.affiche,"realisateur": self.realisateur, "categorie": self.categorie}


class personne(models.Model):
    pseudo = models.CharField(max_length=100)
    nom_prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    #def __str__(self):
       # chaine = f"{self.pseudo} | {self.mail} | {self.nom_prenom} | {self.type} | {self.mot_de_passe}"
        #return chaine

    def dictionnaire(self):
        return {"pseudo": self.pseudo, "nom_prenom": self.nom_prenom, "mail": self.mail,"mot_de_passe": self.mot_de_passe, "type": self.type}


class acteur(models.Model):
    film = models.ManyToManyField(film)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)
    photos = models.FileField(upload_to='', storage=None, null=True, blank=True, default="APLU")

    #def __str__(self):
        #chaine = f"{self.nom} | {self.prenom} | {self.age}"
        #return chaine

    def dictionnaire(self):
        return {"nom": self.nom, "prenom": self.prenom, "âge": self.age, "photos": self.photos,"film": self.film}


class commentaire(models.Model):

    film = models.ForeignKey(film, on_delete=models.CASCADE, default=None, null=True)
    personnes = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    commentaire = models.CharField(max_length=300)
    date = models.DateField()

    #def __str__(self):
       # chaine = f"{self.film} | {self.personnes} | {self.date} | {self.note} | {self.commentaire}"
       # return chaine

    def dictionnaire(self):
        return {"film": self.film, "personnes": self.personnes, "date": self.date, "note": self.note,"commentaire": self.commentaire}

