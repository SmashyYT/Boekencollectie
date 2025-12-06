import sqlite3
from config.settings import DATABASE_PATH

#connecteren met de database
def get_connection():
    return sqlite3.connect(DATABASE_PATH)

#alle boeken ophalen
def fetch_all_books():
    dbconnectie = get_connection()
    cursor = dbconnectie.cursor()
    query="""
    SELECT boeken.id, boeken.titel, auteurs.naam
    FROM boeken
    JOIN auteurs ON boeken.auteur_id = auteurs.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    dbconnectie.close()
    return results

#alle auteurs ophalen
def fetch_all_authors():
    dbconnectie = get_connection()
    cursor = dbconnectie.cursor()
    query="""
    SELECT id, naam 
    FROM auteurs
    """
    cursor.execute(query)
    results = cursor.fetchall()
    dbconnectie.close()
    return results

#toevoegen van boek -> als auteur nog niet bestaat in database, wordt die automatisch aangemaakt
def add_book_with_author(titel, auteur_naam):

    #haal auteur id op, maak nieuwe aan als nodig
    auteur_id = get_or_create_author(auteur_naam.strip())

    #voeg het boek toe met de auteur_id
    dbconnectie = get_connection()
    cursor = dbconnectie.cursor()
    query="""
    INSERT INTO boeken (titel, auteur_id) VALUES (?, ?)
    """
    cursor.execute(query, (titel.strip(), auteur_id))
    dbconnectie.commit()
    dbconnectie.close()
    
    
#auteur id ophalen of creëren als nog niet bestaat
def get_or_create_author(naam):
    dbconnectie = get_connection()
    cursor = dbconnectie.cursor()
    
    #check of auteur al bestaat
    cursor.execute("SELECT id FROM auteurs WHERE naam = ?", (naam,))
    result = cursor.fetchone()
    
    if result:
        auteur_id = result[0]  #auteur bestaat, haal id
    else:
        #auteur bestaat nog niet, voeg toe
        cursor.execute("INSERT INTO auteurs (naam) VALUES (?)", (naam,))
        dbconnectie.commit()
        auteur_id = cursor.lastrowid  #id van nieuw aangemaakte auteur

    dbconnectie.close()
    return auteur_id


    





