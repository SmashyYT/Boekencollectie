from database import fetch_all_books, fetch_all_authors, add_book_with_author, book_exists
from utils.export import export_to_csv
from models.boek import Boek
from models.auteur import Auteur

#menu tonen
def show_menu():
    print("\n===Boekencollectie===")
    print("1. Toon alle boeken")
    print("2. Voeg een boek toe")
    print("3. Toon alle auteurs")
    print("4. Exporteer naar csv-bestand")
    print("5. Afsluiten")
    
    
#boeken tonen
def display_books():
    boeken = fetch_all_books()
    
    if not boeken:
        print("Er zitten nog geen boeken in de collectie.")
    else:
        #kolombreedtes voor mooie uitlijning
        titel_width = max(len(boek.titel) for boek in boeken + [Boek(0, "Titel", "Auteur")])
        auteur_width = max(len(boek.auteur) for boek in boeken + [Boek(0, "Titel", "Auteur")])
        
        print(f"\n{'Titel'.ljust(titel_width)} | {'Auteur'.ljust(auteur_width)}")
        print("-" * (titel_width + auteur_width + 3))
        
        # data
        for boek in boeken:
            print(f"{boek.titel.ljust(titel_width)} | {boek.auteur.ljust(auteur_width)}")
            
#auteurs tonen
def display_authors():
    auteurs = fetch_all_authors()
    
    if not auteurs:
        print("Er zijn nog geen auteurs te vinden.")
    else:
        #kolombreedtes voor mooie uitlijning
        naam_width = max(len(auteur.naam) for auteur in auteurs + [Auteur(0, "Naam")])
        
        print(f"\n{'Naam'.ljust(naam_width)}")
        print("-" * naam_width)
        
        for auteur in auteurs:
            print(f"{auteur.naam.ljust(naam_width)}")
            
#boek toevoegen
def add_book():
    while True:
        titel = input("Titel van het boek: ").strip()
        
        if(titel == ""): 
            print("Titel mag niet leeg zijn, probeer opnieuw alstublieft.")
        else:
            break
        
    while True:
        auteur_naam = input("Naam van de auteur: ").strip()
        
        if(auteur_naam == ""):
            print("Naam van auteur mag niet leeg zijn, probeer opnieuw alstublieft.")
        else:
            break
            
    add_book_with_author(titel, auteur_naam)
    print(f"Het boek '{titel}' van {auteur_naam} werd toegevoegd aan de boekencollectie!")

#csv-bestand aanmaken
def get_csv_file():
    filenaam = input("Geef bestandsnaam (of laat leeg voor standaard): ").strip()
    if(filenaam == ""):
        export_to_csv()
    else:
        if not filenaam.endswith(".csv"):
            filenaam += ".csv"
        export_to_csv(filenaam)
    

    
#hoofdprogramma    
def main():
    while True:
        show_menu()
        keuze = input("Maak een keuze: ").strip()
        
        if keuze == "1":
            display_books()
        elif keuze == "2":
            add_book()
        elif keuze == "3":
            display_authors()
        elif keuze == "4":
            get_csv_file()
        elif keuze == "5":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw alstublieft.")


if __name__ == "__main__":
    main()
