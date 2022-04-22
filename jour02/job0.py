class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Bonjour " + self.nom, self.prenom)
    
    # Accessor

    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom

    # Mutator

    def set_nom(self, nom):
        self.nom = nom
    
    def set_prenom(self, prenom):
        self.prenom = prenom

x = Personne("Python", "GrosBOA")
y = Personne("Dupont", "Michel")
x.SePresenter()
y.SePresenter()
