import sys
import urllib2
import json
from pprint import pprint

deck_api_string = "https://hsreplay.net/analytics/query/list_decks_by_win_rate/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&TimeRange=LAST_30_DAYS"
card_api_string = "https://api.hearthstonejson.com/v1/20970/enUS/cards.collectible.json"

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

def parse_cards_json(file):
    with open(file) as data_file:
        data = json.load(data_file)

    pprint(data)

if __name__ == "__main__":
    #get_from_api(deck_api_string, 'decks.json')
    parse_cards_json('decks.json')
    get_from_api(card_api_string, 'cards.json')
    parse_cards_json('cards.json')
