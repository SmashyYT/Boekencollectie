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

## 4. Position database

Maak een de map data aan en plaats de meegegeven voorbeelddatabase hierin. De map kan je manueel aanmaken, of door de code hieronde uit te voeren in de terminal.

*Windows*
```
mkdir data
```

*Linux, macOS*
```
mkdir -p data
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

2. Toevoegen inhoud en database plaatsen

Navigeer naar de de `config` map en open `settings.py`. 

De inhoud (vervang met de voorbeelddatabase):

```python
DATABASE_PATH = "data/<jouwdatabase>.db"
```

Je kan in het bestand `config\settings_voorbeeld.py` een voorbeeld bekijken.

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

