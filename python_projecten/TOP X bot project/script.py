import requests
from bs4 import BeautifulSoup  

# Haal de HTML-inhoud op van de gespecificeerde URL
url = 'https://boardgamegeek.com/browse/boardgame'  
html = requests.get(url)  

# Parseer de HTML-inhoud met BeautifulSoup
soup = BeautifulSoup(html.content, 'html.parser')  

# Vind de container die de gewenste gegevens bevat
results_container = soup.find(id='collection')  

# Maak een lege dictionary om de spellen op te slaan
games_list = []

# Haal de rijen op in de tabel die de spellen bevatten
game_rows = results_container.find_all('tr', id=lambda x: x and x.startswith('row_'))  

# Itereer over elke rij en haal de rang en titel op
for row in game_rows:  
    rank = row.find('td', class_='collection_rank').text.strip()  
    title = row.find('a', class_='primary').text.strip()  
    
    # Voeg de rang en titel toe aan de dictionary
    games_info = {
        'title' : title,
        'rank' : rank
    }

    games_list.append(games_info)

# Print de dictionary
print(games_list)