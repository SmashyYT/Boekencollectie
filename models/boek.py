class Boek:
    def __init__(self, boek_id, titel, auteur_naam):
        self.id = boek_id
        self.titel = titel
        self.auteur = auteur_naam
        
    def __str__(self):
        return f"{self.titel} ({self.auteur})"
    
    
