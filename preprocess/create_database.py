import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS deck (deck_id int, cards blob, avg_duration int, archetype_id int) ''')
        c.execute('''
                    CREATE TABLE IF NOT EXISTS archetype (id int, name text) ''')
        c.execute('''
                    CREATE TABLE IF NOT EXISTS card (id_dbfid int, name text)''')
        return c
    except Error as e:
        print(e)
        return None

def load_fake_data(c):
    try:
        c.execute('''
                    INSERT INTO card (id_dbfid, name) VALUES (559, 'Leeroy Jenkins')''')
        c.execute('''
                    SELECT * FROM card''')
        print c.fetchone()
    except Error as e:
        print e

if __name__ == "__main__":
    c = create_connection("hs-clock.db")
    load_fake_data(c)
    c.close()
