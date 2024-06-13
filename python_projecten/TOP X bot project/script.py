import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import*

# Stap 1: Scrape de data van BoardGameGeek
url = 'https://boardgamegeek.com/browse/boardgame'
response = requests.get(url)  # Verzendt een GET-verzoek naar de URL
response.raise_for_status()  # Verifieert of het verzoek succesvol was

soup = BeautifulSoup(response.content, 'html.parser')  # Parse de HTML-content van de pagina met BeautifulSoup
rows = soup.find_all('tr', id=lambda x: x and x.startswith('row_'))  # Zoek alle rijen die beginnen met 'row_'

# Stap 2: Maak een SQLite-database en tabellen
create_database()  # Roept een functie aan om de database en vereiste tabellen te maken

# Voeg een nieuw record toe in de visit-tabel
collected_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Haal de huidige datum en tijd op
visit_id = insert_visit(collected_on, url)  # Voeg een bezoekrecord toe aan de database en haal het visit_id op

# Stap 3: Vul de visit_item-tabel met gescrapte data
visit_items = []  # Initialiseer een lege lijst om visit items op te slaan
board_games = []  # Initialiseer een lege lijst om dictionaries van bordspellen op te slaan
for row in rows:  # Loop door elke rij die we eerder vonden
    rank = int(row.find('td', class_='collection_rank').get_text(strip=True))  # Haal de rang op en converteer naar een integer
    name = row.find('td', class_='collection_objectname').get_text(strip=True)  # Haal de naam van het bordspel op
    visit_items.append((visit_id, name, rank))  # Voeg een tuple toe met visit_id, naam en rang
    board_games.append({"title": name, "rank": rank})  # Voeg een dictionary toe aan de lijst met bordspellen

# Voeg visit items toe aan de database
item_ids = insert_visit_items(visit_items)  # Voeg de verzamelde visit items toe aan de database en haal de item_ids op

# Vul de visit_item_info-tabel met extra data
visit_item_info = []  # Initialiseer een lege lijst om visit item info op te slaan
for item_id, row in zip(item_ids, rows):  # Loop door de item_ids en rijen
    geek_rating = row.find('td', class_='collection_bggrating').get_text(strip=True) if row.find('td', class_='collection_bggrating') else "N/A"  # Haal de geek rating op
    year_published = row.find('td', class_='collection_year').get_text(strip=True) if row.find('td', class_='collection_year') else "Unknown"  # Haal het jaar van publicatie op
    description = row.find('p', class_='sm_description').get_text(strip=True) if row.find('p', class_='sm_description') else "No description available"  # Haal de beschrijving op
    visit_item_info.extend([
        (item_id, "GEEK RATING", geek_rating),
        (item_id, "YEAR", year_published),
        (item_id, "DESCRIPTION", description)
    ])  # Voeg tuples toe met item_id, veldnaam en veldwaarde

# Voeg visit item info toe aan de database
insert_visit_item_info(visit_item_info)  # Voeg de verzamelde visit item info toe aan de database

# Print de lijst van bordspellen
print("Database is succesvol gevuld.")
print("Lijst van bordspellen met titel en rang:")
for game in board_games:  # Loop door elk bordspel in de lijst
    print(game)  # Print de titel en rang van het bordspel


