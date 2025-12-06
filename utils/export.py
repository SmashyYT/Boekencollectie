import csv
from database import fetch_all_books

def export_to_csv(filenaam = "boekencollectie.csv"):
    boeken = fetch_all_books()
    
    if not boeken:
        print("Er zitten nog geen boeken in de collectie.")
        return
              
    try:
        with open(filenaam, 'w', newline='', encoding="utf-8-sig") as boekencollectie:
            writer = csv.writer(boekencollectie, delimiter=",", quoting=csv.QUOTE_ALL)
            
            header = ["ID", "Titel", "Auteur"]
            writer.writerow(header)
            
            for boek in boeken:
                writer.writerow(boek)
            
            print(f"Export succesvol! Bestand werd opgeslagen als '{filenaam}' en is terug te vinden in uw projectfolder.")
    except Exception as e:
        print(f"Er ging iets mis bij het exporteren: {e}")
                
        
