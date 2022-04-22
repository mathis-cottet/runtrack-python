class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def ShowName(self):
        print("nom:" + self.nom , "prenom: " + self.prenom)

class Auteur(Personne):
    def __init__(self, nom, prenom):
        self.oeuvre = []
        
    def listerOeuvre(self):
        return (print(self.oeuvre))
        
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre.titre)
        


class Livre(Auteur):
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
    
        

x = Auteur("Python","GrosBOA")
x.ecrireUnLivre("l'art de mourir")
x.ecrireUnLivre("MarsAttack")
x.listerOeuvre()
x = Personne("dupont", "lascience")
x.ShowName()



