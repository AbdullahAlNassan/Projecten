import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import *

# Stap 1: Scrape de data van BoardGameGeek
url = 'https://boardgamegeek.com/browse/boardgame'
response = requests.get(url)
response.raise_for_status()  # Controleer of het verzoek succesvol was

soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr', id=lambda x: x and x.startswith('row_'))

# Stap 2: Maak een SQLite-database en tabellen
create_database()

# Voeg een nieuw record toe in de visit-tabel
collected_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
visit_id = insert_visit(collected_on, url)

# Stap 3: Vul de visit_item-tabel met gescrapte data
visit_items = []
board_games = []
for row in rows:
    rank = int(row.find('td', class_='collection_rank').get_text(strip=True))  # Haal de rang op
    name = row.find('td', class_='collection_objectname').get_text(strip=True)  # Haal de naam op
    visit_items.append((visit_id, name, rank))
    board_games.append({"title": name, "rank": rank})

# Voeg visit items toe aan de database
item_ids = insert_visit_items(visit_items)

# Vul de visit_item_info-tabel met extra data
visit_item_info = []
for item_id, row in zip(item_ids, rows):
    geek_rating = row.find('td', class_='collection_bggrating').get_text(strip=True) if row.find('td', class_='collection_bggrating') else "N/A"  # Haal de geek rating op
    year_published = row.find('td', class_='collection_year').get_text(strip=True) if row.find('td', class_='collection_year') else "Unknown"  # Haal het jaar van publicatie op
    description = row.find('p', class_='sm_description').get_text(strip=True) if row.find('p', class_='sm_description') else "No description available"  # Haal de beschrijving op
    visit_item_info.extend([
        (item_id, "GEEK RATING", geek_rating),
        (item_id, "YEAR", year_published),
        (item_id, "DESCRIPTION", description)
    ])

# Voeg visit item info toe aan de database
insert_visit_item_info(visit_item_info)

# Print de lijst van bordspellen
print("Lijst van bordspellen met titel en rank:")
for game in board_games:
    print(game)
print("Database is succesvol gevuld.")