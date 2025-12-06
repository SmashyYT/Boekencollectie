from database import fetch_all_books, fetch_all_authors, add_book_with_author

#menu tonen
def show_menu():
    print("\n===Boekencollectie===")
    print("1. Toon alle boeken")
    print("2. Voeg een boek toe")
    print("3. Toon alle auteurs")
    print("4. Afsluiten")
    
    
#boeken tonen
def display_books():
    boeken = fetch_all_books()
    
    if not boeken:
        print("Er zitten nog geen boeken in de collectie.")
    else:
        print("\nTitel | Auteur")
        print("-" * 30)
        for boek in boeken:
            print(f"{boek[1]} | {boek[2]}")
            

        
    
#hoofdprogramma    
def main():
    while True:
        show_menu()
        keuze = input("Maak een keuze: ").strip()
        
        if keuze = "1":
            display_books()
        elif keuze = "2":
            #voeg boek toe
        elif keuze = "3":
            #toon auteurs
        elif keuze = "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw alstublieft.")






if __name__ == "__main__":
    main()
