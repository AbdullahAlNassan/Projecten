import sqlite3



def create_database():
    # Maak verbinding met de SQLite-database en maak de vereiste tabellen aan
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor() 
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS visit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            collected_on TEXT,
            url TEXT
        );
        CREATE TABLE IF NOT EXISTS visit_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visit_id INTEGER,
            name TEXT,
            rank INTEGER,
            FOREIGN KEY(visit_id) REFERENCES visit(id)
        );
        CREATE TABLE IF NOT EXISTS visit_item_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visit_item_id INTEGER,
            key TEXT,
            value TEXT,
            FOREIGN KEY(visit_item_id) REFERENCES visit_item(id)
        );
        CREATE TABLE IF NOT EXISTS boardgame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            rank INTEGER
        );
    ''')  
    conn.commit()  # Sla de wijzigingen op
    conn.close()  # Sluit de verbinding

def insert_visit(collected_on, url):
    # Voeg een record toe aan de 'visit' tabel
    conn = sqlite3.connect('boardgames.db') 
    cursor = conn.cursor()
    cursor.execute('INSERT INTO visit (collected_on, url) VALUES (?, ?)', (collected_on, url))
    visit_id = cursor.lastrowid  # Haal het ID van het laatste toegevoegde record op
    conn.commit()  # Sla de wijzigingen op
    conn.close()  # Sluit de verbinding
    return visit_id

def insert_visit_items(visit_items):
    # Voeg meerdere records toe aan de 'visit_item' tabel
    conn = sqlite3.connect('boardgames.db') 
    cursor = conn.cursor() 
    cursor.executemany('INSERT INTO visit_item (visit_id, name, rank) VALUES (?, ?, ?)', visit_items) 
    conn.commit()  # Sla de wijzigingen op
    cursor.execute('SELECT id FROM visit_item ORDER BY id DESC LIMIT ?', (len(visit_items),))
    item_ids = [item_id[0] for item_id in cursor.fetchall()]  # Haal de IDs van de toegevoegde records op
    conn.close()  # Sluit de verbinding
    return item_ids

def insert_visit_item_info(visit_item_info):
    # Voeg meerdere records toe aan de 'visit_item_info' tabel
    conn = sqlite3.connect('boardgames.db') 
    cursor = conn.cursor()  
    cursor.executemany('INSERT INTO visit_item_info (visit_item_id, key, value) VALUES (?, ?, ?)', visit_item_info)  
    conn.commit()  # Sla de wijzigingen op
    conn.close()  # Sluit de verbinding

def insert_boardgames(boardgames):
    # Voeg meerdere records toe aan de 'boardgame' tabel
    conn = sqlite3.connect('boardgames.db')  
    cursor = conn.cursor()  
    cursor.executemany('INSERT INTO boardgame (title, rank) VALUES (?, ?)', boardgames)  
    conn.commit()  # Sla de wijzigingen op
    conn.close()  # Sluit de verbinding


    
