# General description

Een app die een kleine boekendatabase beheert via een command-line menu. 
Je kan boeken toevoegen, gelezen boeken en auteurs bekijken en exporteren naar een csv-bestand.
Op deze manier kan je gemakkelijk bijhouden welke boeken je gelezen hebt. 

# How to operate
## 1. Clone de repository

```
git clone <github-url>
cd boekencollectie
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

# Settings file

Dit bestand staat niet in de repository omdat het de database locatie bevat (gevoelige informatie).
Er zit wel een voorbeeldbestand `settings_example.py` in de repository.

De inhoud van settings.py moet zijn:

```python
DATABASE_PATH = "data/<databasenaam>.db"
```

# Requirements

Python 3.10+ wordt aanbevolen.

# Author

Jarne Van de Kerkhof
Student Toegepaste Informatica te Vives Kortrijk (bachelor, afstandsonderwijs).

Gemaakt als oefenproject voor het vak 'Programmeren in Python'.

