import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# Step 1: Scrape the data from BoardGameGeek
url = 'https://boardgamegeek.com/browse/boardgame'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr', id=lambda x: x and x.startswith('row_'))

# Step 2: Create a SQLite database
conn = sqlite3.connect('boardgames.db')
cursor = conn.cursor()

# Create visit table
cursor.execute('''
CREATE TABLE IF NOT EXISTS visit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    collected_on TEXT,
    url TEXT
)
''')

# Create visit_item table
cursor.execute('''
CREATE TABLE IF NOT EXISTS visit_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visit_id INTEGER,
    name TEXT,
    rank INTEGER,
    FOREIGN KEY(visit_id) REFERENCES visit(id)
)
''')

# Insert a new record in visit table
collected_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('INSERT INTO visit (collected_on, url) VALUES (?, ?)', (collected_on, url))
visit_id = cursor.lastrowid

# Step 3: Populate visit_item table with scraped data
for row in rows:
    rank = int(row.find('td', class_='collection_rank').get_text(strip=True))
    name = row.find('td', class_='collection_objectname').get_text(strip=True)
    cursor.execute('INSERT INTO visit_item (visit_id, name, rank) VALUES (?, ?, ?)', (visit_id, name, rank))

# Commit and close the database connection
conn.commit()
conn.close()

print("Database has been populated successfully.")
