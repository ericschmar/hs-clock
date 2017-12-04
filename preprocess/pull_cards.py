import sys
import urllib2
import json
import sqlite3
from create_database import create_database
from deck import deck
from card import card
from archetype import archetype
from pprint import pprint
from sqlite3 import Error

deck_api_string = "https://hsreplay.net/analytics/query/list_decks_by_win_rate/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&TimeRange=LAST_30_DAYS"
card_api_string = "https://api.hearthstonejson.com/v1/20970/enUS/cards.collectible.json"
archetype_api_string = "https://hsreplay.net/api/v1/archetypes/?format=json"

def get_from_api(target, f_name):
    url = target
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}


    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    if target == deck_api_string:
        content = page.read().replace("\\", "")
        print content[:1000]
    else:
        content = page.read()

    f = open(f_name, 'w')
    f.write(content)

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
    #    decks[i].print_deck()
    return decks

def parse_cards_json(file):
    with open(file) as data_file:
        data = json.load(data_file)

    cards = []
    for i in range(len(data)):
        m = data[i]
        #pprint(m)
        if 'SPELL' == m['type']:
            c = card(id=m['dbfId'], name=m['name'], cost=m['cost'], attack="Null", health="Null", card_type=m['type'])
            #c.print_card()
        elif 'MINION' == m['type']:
            c = card(id=m['dbfId'], name=m['name'], cost=m['cost'], attack=m['attack'], health=m['health'], card_type=m['type'])
            #c.print_card()
        elif 'HERO' == m['type']:
            pass
        else:
            c = card(id=m['dbfId'], name=m['name'], cost=m['cost'], attack="Null", health="Null", card_type=m['type'])
            #c.print_card()
        cards.append(c)

    #for i in range(len(cards)):
    #    cards[i].print_card()
    return cards

def parse_archetypes_json(file):
    with open(file) as data_file:
        data = json.load(data_file)

    archetypes = []

    for i in range(len(data)):
        m = data[i]
        a = archetype(arch_id=m["id"], name=m["name"], player_class=m["player_class_name"])
        archetypes.append(a)

    #for i in range(len(archetypes)):
    #    archetypes[i].print_archetype()

    return archetypes

def populate_database(db_file="hs-clock.db"):
    try:
        c = create_database('hs-clock.db')
        cards = parse_cards_json('cards.json')
        decks = parse_decks_json('decks.json')
        archetypes = parse_archetypes_json('archetypes.json')

        for i in range(len(cards)):
            card = cards[i]
            c.execute('''INSERT INTO CARD (id_dbfid, name, cost, attack, health, type) VALUES ({}, '{}', {}, {}, {}, '{}') 
                    '''.format(card.id, card.name, card.cost, card.attack, card.health, card.card_type))
            c.commit()

        for i in range(len(decks)):
            deck = decks[i]
            c.execute(''' INSERT INTO DECK (deck_id, deck_list, avg_duration, archetype_id, turns, digest, win_rate, class) VALUES ({}, {}, {}, {}, {}, '{}', {}, '{}')'''.format(deck.id, deck.deck_list, deck.game_length, "Null", deck.turns, deck.digest, deck.win_rate, deck.player_class))
            c.commit()

        for i in range(len(archetypes)):
            archetype = archetypes[i]
            archetype.print_archetype()
            c.execute(''' INSERT INTO ARCHETYPE (id, name, player_class_name) VALUES ({}, '{}', '{}')'''.format(archetype.arch_id, archetype.name, archetype.player_class))
            c.commit()
            
    except Error as e:
        print(e)

if __name__ == "__main__":
    get_from_api(deck_api_string, 'decks.json')
    parse_decks_json('decks.json')
    get_from_api(card_api_string, 'cards.json')
    parse_cards_json('cards.json')
    get_from_api(archetype_api_string, 'archetypes.json')
    parse_archetypes_json('archetypes.json')
    populate_database()
