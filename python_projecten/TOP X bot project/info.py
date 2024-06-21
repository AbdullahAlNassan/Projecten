import sqlite3 

def fetch_all(query, params=()):
    conn = sqlite3.connect('boardgames.db') 
    cursor = conn.cursor()  
    cursor.execute(query, params) 
    results = cursor.fetchall() 
    conn.close()
    return results 

def list_visits():
    # Haal alle records op uit de 'visit' tabel
    visits = fetch_all('SELECT id, collected_on, url FROM visit') 
    print("Visits:")
    for visit in visits:
        print(f"{visit[0]}: {visit[1]} {visit[2]}") 
    return visits

def list_visit_items(visit_id):
    # Haal alle items op voor een gegeven visit_id uit de 'visit_item' tabel
    items = fetch_all('SELECT id, name, rank FROM visit_item WHERE visit_id = ?', (visit_id,)) 
    print("\nVisit items:")
    print("VISIT  ID   NAME                          RANK") 
    print('-' * 50) 
    for item in items:
        print(f"{visit_id}      {item[0]}    {item[1]} {item[2]}")

def list_visit_item_info(visit_item_id):
    # Haal alle informatie op voor een gegeven visit_item_id uit de 'visit_item_info' tabel
    info = fetch_all('SELECT key, value FROM visit_item_info WHERE visit_item_id = ?', (visit_item_id,))  
    print("\nVisit item info:")  
    for item in info:
        print(f"{item[0]}: {item[1]}") 

def main():
    while True:
        # Lijst van alle bezoeken
        visits = list_visits()
        
        visit_input = input("\nDruk op bezoeknummer om bezoekitems te tonen of 'X' om te stoppen: ")
        if visit_input.lower() == 'x':
            break

        try:
            visit_id = int(visit_input)
            if any(visit[0] == visit_id for visit in visits):
                # Lijst van items voor het geselecteerde bezoek
                list_visit_items(visit_id)
                item_input = input("\nDruk op itemnummer om iteminfo te tonen of 'X' om terug te gaan: ")
                if item_input.lower() == 'x':
                    continue

                try:
                    item_id = int(item_input)
                    # Lijst van informatie voor het geselecteerde item
                    list_visit_item_info(item_id)
                except ValueError:
                    print("Ongeldige invoer. Voer een geldig itemnummer in of 'X' om terug te gaan.")
            else:
                print("Ongeldig bezoeknummer.")
        except ValueError:
            print("Ongeldige invoer. Voer een geldig bezoeknummer in of 'X' om te stoppen.")

main()

