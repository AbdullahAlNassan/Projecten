from script import *
import sqlite3


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

# Commit de wijzigingen en sluit de verbinding
conn.commit()
conn.close()