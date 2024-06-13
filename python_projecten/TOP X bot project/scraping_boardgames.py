import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import create_database, insert_visit, insert_visit_items, insert_visit_item_info

# Step 1: Scrape the data from BoardGameGeek
url = 'https://boardgamegeek.com/browse/boardgame'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr', id=lambda x: x and x.startswith('row_'))

# Step 2: Create a SQLite database and tables
create_database()

# Insert a new record in visit table
collected_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
visit_id = insert_visit(collected_on, url)

# Step 3: Populate visit_item table with scraped data
visit_items = []
visit_item_info = []
for row in rows:
    rank = int(row.find('td', class_='collection_rank').get_text(strip=True))
    name = row.find('td', class_='collection_objectname').get_text(strip=True)
    visit_items.append((visit_id, name, rank))

# Insert visit items into the database
item_ids = insert_visit_items(visit_items)

# Populate visit_item_info table with additional data
for item_id, row in zip(item_ids, rows):
    geek_rating = row.find('td', class_='collection_bggrating').get_text(strip=True) if row.find('td', class_='collection_bggrating') else "N/A"
    year_published = row.find('td', class_='collection_year').get_text(strip=True) if row.find('td', class_='collection_year') else "Unknown"
    description = row.find('p', class_='sm_description').get_text(strip=True) if row.find('p', class_='sm_description') else "No description available"
    
    visit_item_info.append((item_id, "GEEK RATING", geek_rating))
    visit_item_info.append((item_id, "YEAR", year_published))
    visit_item_info.append((item_id, "DESCRIPTION", description))

# Insert visit item info into the database
insert_visit_item_info(visit_item_info)

print("Database has been populated successfully.")
