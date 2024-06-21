import sqlite3  # Importeert de sqlite3 module om met SQLite-databases te werken

def create_database():
    conn = sqlite3.connect('boardgames.db')  # Verbindt met (of maakt) de database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
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
    ''')  # Voert een SQL script uit om de tabellen te maken, indien ze nog niet bestaan
    conn.commit()  # Slaat de wijzigingen op in de database
    conn.close()  # Sluit de database verbinding

def insert_visit(collected_on, url):
    conn = sqlite3.connect('boardgames.db')  # Verbindt met de database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
    cursor.execute('INSERT INTO visit (collected_on, url) VALUES (?, ?)', (collected_on, url))  # Voert een SQL query uit om een record toe te voegen aan de 'visit' tabel
    visit_id = cursor.lastrowid  # Haalt het id op van het laatste ingevoegde record
    conn.commit()  # Slaat de wijzigingen op in de database
    conn.close()  # Sluit de database verbinding
    return visit_id  # Geeft het visit_id terug

def insert_visit_items(visit_items):
    conn = sqlite3.connect('boardgames.db')  # Verbindt met de database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
    cursor.executemany('INSERT INTO visit_item (visit_id, name, rank) VALUES (?, ?, ?)', visit_items)  # Voert een SQL query uit om meerdere records toe te voegen aan de 'visit_item' tabel
    conn.commit()  # Slaat de wijzigingen op in de database
    cursor.execute('SELECT id FROM visit_item ORDER BY id DESC LIMIT ?', (len(visit_items),))  # Voert een SQL query uit om de laatst toegevoegde item_ids op te halen
    item_ids = [item_id[0] for item_id in cursor.fetchall()]  # Maakt een lijst van de opgehaalde item_ids
    conn.close()  # Sluit de database verbinding
    return item_ids  # Geeft de item_ids terug

def insert_visit_item_info(visit_item_info):
    conn = sqlite3.connect('boardgames.db')  # Verbindt met de database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
    cursor.executemany('INSERT INTO visit_item_info (visit_item_id, key, value) VALUES (?, ?, ?)', visit_item_info)  # Voert een SQL query uit om meerdere records toe te voegen aan de 'visit_item_info' tabel
    conn.commit()  # Slaat de wijzigingen op in de database
    conn.close()  # Sluit de database verbinding

def insert_boardgames(boardgames):
    conn = sqlite3.connect('boardgames.db')  # Verbindt met de database 'boardgames.db'
    cursor = conn.cursor()  # Maakt een cursor object om SQL queries uit te voeren
    cursor.executemany('INSERT INTO boardgame (title, rank) VALUES (?, ?)', boardgames)  # Voert een SQL query uit om meerdere records toe te voegen aan de 'boardgame' tabel
    conn.commit()  # Slaat de wijzigingen op in de database
    conn.close()  # Sluit de database verbinding
