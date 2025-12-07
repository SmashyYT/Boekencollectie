# General description

Een app die een kleine boekendatabase beheert via een command-line menu. 
Je kan boeken toevoegen, gelezen boeken en auteurs bekijken en exporteren naar een csv-bestand.
Op deze manier kan je gemakkelijk bijhouden welke boeken je gelezen hebt. 

# How to operate
## 1. Clone the repository

```
git clone <github-url>
cd Boekencollectie
```

## 2. Use virtual environment (optional)

Deze stap is optioneel omdat we geen externe packages gebruiken.

*Windows*
```
python -m venv .venv
.venv\Scripts\activate
```

*Linux, macOS*
```
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install packages

Er zijn geen externe packages nodig, dus voor deze stap hoef je niets te doen!
De `requirements.txt` blijft leeg maar zit in de repository omdat dit best practice is.

## 4. Setup database

In de repository zitten 2 databases (in de map `data`):
1. Een voorbeelddatabase `boekencollectie_voorbeeld.db`. Hierin zit voorbeelddata. Deze kan gebruikt worden om de functionaliteiten van de app te leren kennen.

2. Een lege database `boekencollectie_leeg.db`. Hierin zit geen data. Maak hier een kopie van als eigen werkdatabase.

*Windows*
```
copy data\boekencollectie_leeg.db data\boekencollectie.db
```

*Linux, macOS*
```
cp data/boekencollectie_leeg.db data/boekencollectie.db
```

## 5. Setup settings file

1. Maak een bestand `settings.py` aan in de `config` map. Dit kan je manueel doen, of door de code hieronder uit te voeren in de terminal.

*Windows*
```
type nul > config\settings.py
```

*Linux, macOS*
```
touch config/settings.py
```

2. Toevoegen inhoud 

Als je het voorbeeldbestand gebruikt, is dit de inhoud:

```python
DATABASE_PATH = "data/boekencollectie_voorbeeld.db"
```

Als je je eigen werkbestand (dat in stap 4 werd aangemaakt) gebruikt, is dit de inhoud:

```python
DATABASE_PATH = "data/boekencollectie.db"
```

## 6. Run app

*Windows*
```
python main.py
```

*Linux, macOS*
```
python3 main.py
```

# Requirements

Python 3.10+ wordt aanbevolen.

# Author

Jarne Van de Kerkhof
Student Toegepaste Informatica te Vives Kortrijk (bachelor, afstandsonderwijs).

Gemaakt als oefenproject voor het vak 'Programmeren in Python'.

