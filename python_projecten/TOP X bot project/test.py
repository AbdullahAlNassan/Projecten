import requests
from bs4 import BeautifulSoup  
import sqlite3
from datetime import datetime

# Function to scrape board game data
def scrape_board_games(url):
    html = requests.get(url)  
    soup = BeautifulSoup(html.content, 'html.parser')  
    results_container = soup.find(id='collection')  
    games_list = []

    game_rows = results_container.find_all('tr', id=lambda x: x and x.startswith('row_'))  

    for row in game_rows:  
        rank = row.find('td', class_='collection_rank').text.strip()  
        title = row.find('a', class_='primary').text.strip()  
        games_info = {
            'title': title,
            'rank': rank
        }
        games_list.append(games_info)

    return games_list

# URL of the webpage to scrape
url = 'https://boardgamegeek.com/browse/boardgame'

# Scrape board game data
games_list = scrape_board_games(url)

# Database

# Maak een nieuwe SQLite-databaseverbinding
conn = sqlite3.connect('boardgames.db')

# Creëer een cursorobject om query's uit te voeren
cursor = conn.cursor()

# Creëer een tabel om de spelinformatie op te slaan
cursor.execute('''CREATE TABLE IF NOT EXISTS boardgames
                  (title TEXT, rank INTEGER)''')

# Lus door elk spel in de lijst en voeg het toe aan de database
for game in games_list:
    cursor.execute("INSERT INTO boardgames (title, rank) VALUES (?, ?)", (game['title'], game['rank']))

# Creëer een tabel om de bezoekinformatie op te slaan
cursor.execute('''CREATE TABLE IF NOT EXISTS visits
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   collected_on TEXT,
                   url TEXT)''')

# Voeg informatie over het bezoek toe aan de tabel
collected_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Huidige datum en tijd
cursor.execute("INSERT INTO visits (collected_on, url) VALUES (?, ?)", (collected_on, url))

# Haal het id op van het laatst toegevoegde record in de visits tabel
visit_id = cursor.lastrowid

# Creëer een tabel om de items van het bezoek op te slaan
cursor.execute('''CREATE TABLE IF NOT EXISTS visit_items
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   visit_id INTEGER,
                   name TEXT,
                   rank INTEGER)''')

# Voeg elk item uit games_list toe aan de visit_items tabel met het juiste visit_id
for game in games_list:
    cursor.execute("INSERT INTO visit_items (visit_id, name, rank) VALUES (?, ?, ?)", (visit_id, game['title'], game['rank']))

# Commit de wijzigingen en sluit de verbinding
conn.commit()
conn.close()
