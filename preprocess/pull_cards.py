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
        #content.replace("{\"render_as\":\"table\",\"series\":{\"metadata\":{\"DRUID\":{},\"HUNTER\":{},\"MAGE\":{},\"PALADIN\":{},\"PRIEST\":{},\"ROGUE\":{},\"SHAMAN\":{},\"WARLOCK\":{},\"WARRIOR\":{}},\"data\":", "")
        #content = content[:len(content) - 35] # remove the time of request
    else:
        content = page.read()

    f = open(f_name, 'w')
    f.write(json.dumps(content, sort_keys=True))

def parse_cards_json():
    with open('decks.json') as data_file:
        data = json.load(data_file)

    #pprint(data)
    #for i in data:
    #    print data[i]
    #    print "-------------"

if __name__ == "__main__":
    get_from_api(deck_api_string, 'decks.json')
    parse_cards_json()
    #get_from_api(card_api_string, 'cards.json')
