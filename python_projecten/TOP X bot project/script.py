import requests  
from bs4 import BeautifulSoup 


def scrape_board_games(url):
    # Een HTTP GET-verzoek doen om de HTML-inhoud van de webpagina op te halen
    html = requests.get(url)  
    # De HTML-inhoud parseren met BeautifulSoup
    soup = BeautifulSoup(html.content, 'html.parser')  
    # De container vinden die de collectie bordspellen bevat
    results_container = soup.find(id='collection')  
    # Een lege lijst initialiseren om de spelgegevens op te slaan
    games_list = []

    # Alle rijen in de tabel vinden die individuele bordspellen vertegenwoordigen
    game_rows = results_container.find_all('tr', id=lambda x: x and x.startswith('row_'))  

    # Itereren over elke rij om de speldetails te extraheren
    for row in game_rows:  
        # De rang van het spel extraheren uit de juiste tabelcel
        rank = row.find('td', class_='collection_rank').text.strip()  
        # De titel van het spel extraheren uit de juiste anker-tag
        title = row.find('a', class_='primary').text.strip()  
        # Een woordenboek maken om de titel en rang van het spel op te slaan
        games_info = {
            'title': title,
            'rank': rank
        }
        # De spelinformatie toevoegen aan de games_list
        games_list.append(games_info)

    # De lijst van spellen met hun titels en rangen retourneren
    return games_list

# URL van de webpagina om te scrapen
url = 'https://boardgamegeek.com/browse/boardgame'

# Bordspelgegevens scrapen door de functie aan te roepen met de URL
games_list = scrape_board_games(url)

# De lijst van spellen met hun titels en rangen afdrukken
print(games_list)


