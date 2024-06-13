import sqlite3

def create_database():
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

    # Create visit_item_info table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS visit_item_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visit_item_id INTEGER,
        key TEXT,
        value TEXT,
        FOREIGN KEY(visit_item_id) REFERENCES visit_item(id)
    )
    ''')

    conn.commit()
    conn.close()

def insert_visit(collected_on, url):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO visit (collected_on, url) VALUES (?, ?)', (collected_on, url))
    visit_id = cursor.lastrowid

    conn.commit()
    conn.close()
    
    return visit_id

def insert_visit_items(visit_items):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO visit_item (visit_id, name, rank) VALUES (?, ?, ?)', visit_items)
    conn.commit()
    
    cursor.execute('SELECT id FROM visit_item ORDER BY id DESC LIMIT ?', (len(visit_items),))
    item_ids = cursor.fetchall()
    
    conn.close()
    return [item_id[0] for item_id in item_ids]

def insert_visit_item_info(visit_item_info):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO visit_item_info (visit_item_id, key, value) VALUES (?, ?, ?)', visit_item_info)

    conn.commit()
    conn.close()
