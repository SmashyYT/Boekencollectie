class Auteur:
    def __init__(self, auteur_id, naam):
        self.id = auteur_id
        self.naam = naam

    def __str__(self):
        return self.naam
