import sqlite3
from sqlite3 import Error


def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS deck (deck_id int, deck_list text, avg_duration int, archetype_id int, turns int, digest text, win_rate float, class text) ''')
        c.execute('''
                    CREATE TABLE IF NOT EXISTS archetype (id int, name text, player_class_name text) ''')
        c.execute('''
                    CREATE TABLE IF NOT EXISTS card (id_dbfid int, name text, cost int, attack int, health int, type text)''')
        return conn
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
    c = create_database("hs-clock.db")
    #load_fake_data(c)
    c.close()
