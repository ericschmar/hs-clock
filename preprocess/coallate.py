import sys
import json
from deck import deck
from card import card
from archetype import archetype
import sqlite3
from sqlite3 import Error

total_decks = 0

def parse_decks_json(file):
    with open(file) as data_file:
        data = json.load(data_file)

    d = data['series']
    decks = []
    for i in range(len(d['data'])):
        keys = d['data'].keys()
        items = d['data'][keys[i]]
        for j in range(len(items)):
            m = items[j]
            c = deck(
                    id=m['archetype_id'], 
                    game_length=m['avg_game_length_seconds'], 
                    turns=m['avg_num_player_turns'], 
                    deck_id=m['deck_id'], 
                    deck_list=m['deck_list'], 
                    digest=m['digest'], 
                    win_rate=m['win_rate'],
                    player_class=keys[i])
            decks.append(c)
    #for i in range(len(decks)):
     #   decks[i].print_deck()
    return decks

def count_archetypes(decks):
    global total_decks
    total_decks = len(decks)
    archs = {}
    for i in range(len(decks)):
        if decks[i].id not in archs:
            archs[decks[i].id] = 1
        else:
            archs[decks[i].id] += 1
    
    return archs
        
def save_deck_counts(filename):
    global total_decks
    conn = sqlite3.connect("hs-clock.db")
    c = conn.cursor()
    f = open(filename, 'w')
    archs = count_archetypes(parse_decks_json("decks.json"))
    top_archs = {}
    sorted_decks = sorted(archs.iteritems(), key=lambda (k,v): (v,k))[::-1] 
    for i in range(len(sorted_decks[0:5])):
        c.execute("SELECT id, name FROM archetype WHERE id=?", (sorted_decks[i][0], ))
        row = c.fetchall()
        top_archs[row[0][1]] = { "id":row[0][0], "count":sorted_decks[i][1] } 
    top_archs["total"] = total_decks

    print top_archs

    s = json.dumps(top_archs, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    print "top archs" 
    print s
    f.write(s)
        
if __name__ == "__main__":
    save_deck_counts("deck_counts/initial.json")
        
        
