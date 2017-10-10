import sys
import json
from pprint import pprint

class deck:
    def __init__(self, id=None, game_length=None, turns=None, deck_id=None, deck_list=None, digest=None, win_rate=None, player_class=None):
        self.id = id
        self.game_length = game_length
        self.turns = turns
        self.deck_id = deck_id
        self.deck_list = json.dumps(deck_list)
        self.digest = ''.join(e for e in digest if e.isalnum())
        self.win_rate = win_rate
        self.player_class = ''.join(e for e in player_class if e.isalnum())

    def print_deck(self):
        pprint(vars(self))
