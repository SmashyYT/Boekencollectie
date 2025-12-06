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


    





