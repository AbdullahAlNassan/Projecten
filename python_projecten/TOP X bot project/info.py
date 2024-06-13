import sqlite3  # Importeert de sqlite3 module om met SQLite-databases te werken

# Algemene functie om alle resultaten van een query op te halen
def fetch_all(query, params=()):
    conn = sqlite3.connect('boardgames.db')  # Verbindt met de SQLite-database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
    cursor.execute(query, params)  # Voert de query uit met eventuele parameters
    results = cursor.fetchall()  # Haalt alle resultaten van de query op
    conn.close()  # Sluit de database verbinding
    return results  # Geeft de resultaten terug

# Functie om alle bezoeken (visits) op te sommen
def list_visits():
    visits = fetch_all('SELECT id, collected_on, url FROM visit')  # Haalt alle bezoeken op uit de 'visit' tabel
    print("Visits:")  # Print de header 'Visits:'
    for visit in visits:  # Loop door elk bezoek in de resultaten
        print(f"{visit[0]}: {visit[1]} {visit[2]}")  # Print het id, de verzameltijd en de url van het bezoek
    return visits  # Geeft de lijst met bezoeken terug

# Functie om items van een specifiek bezoek op te sommen
def list_visit_items(visit_id):
    items = fetch_all('SELECT id, name, rank FROM visit_item WHERE visit_id = ?', (visit_id,))  # Haalt items van een specifiek bezoek op uit de 'visit_item' tabel
    print("\nVisit items:")  # Print de header 'Visit items:'
    print("VISIT ID   ID   NAME                          RANK")  # Print de kolomkoppen
    print('-' * 50)  # Print een scheidingslijn
    for item in items:  # Loop door elk item in de resultaten
        print(f"{visit_id}          {item[0]}    {item[1]} {item[2]}")  # Print het bezoek id, item id, naam en rang van het item

# Functie om informatie van een specifiek visit_item op te sommen
def list_visit_item_info(visit_item_id):
    info = fetch_all('SELECT key, value FROM visit_item_info WHERE visit_item_id = ?', (visit_item_id,))  # Haalt informatie van een specifiek visit_item op uit de 'visit_item_info' tabel
    print("\nVisit item info:")  # Print de header 'Visit item info:'
    for item in info:  # Loop door elk item in de resultaten
        print(f"{item[0]}: {item[1]}")  # Print de sleutel en waarde van het item

# Hoofdfunctie om de gebruikersinteractie te beheren
def main():
    while True:  # Oneindige lus om door te gaan tot de gebruiker kiest om te stoppen
        visits = list_visits()  # Roep de functie aan om alle bezoeken op te sommen
        
        visit_input = input("\nPress visit number to show visit items or 'X' to exit: ")  # Vraag de gebruiker om een bezoeknummer of 'X' om te stoppen
        if visit_input.lower() == 'x':  # Controleer of de gebruiker 'X' heeft ingevoerd
            break  # Stop de lus en beëindig het programma

        try:
            visit_id = int(visit_input)  # Probeer de invoer te converteren naar een integer
            if any(visit[0] == visit_id for visit in visits):  # Controleer of het ingevoerde visit_id bestaat
                list_visit_items(visit_id)  # Roep de functie aan om items van het specifieke bezoek op te sommen
                item_input = input("\nPress item number to show item info or 'X' to go back: ")  # Vraag de gebruiker om een itemnummer of 'X' om terug te gaan
                if item_input.lower() == 'x':  # Controleer of de gebruiker 'X' heeft ingevoerd
                    continue  # Ga terug naar het begin van de lus

                try:
                    item_id = int(item_input)  # Probeer de invoer te converteren naar een integer
                    list_visit_item_info(item_id)  # Roep de functie aan om informatie van het specifieke item op te sommen
                except ValueError:  # Vang de fout als de invoer geen geldige integer is
                    print("Invalid input. Please enter a valid item number or 'X' to go back.")  # Print een foutmelding
            else:
                print("Invalid visit number.")  # Print een foutmelding als het visit_id niet bestaat
        except ValueError:  # Vang de fout als de invoer geen geldige integer is
            print("Invalid input. Please enter a valid visit number or 'X' to exit.")  # Print een foutmelding

# Start het programma door de main functie aan te roepen
main()

