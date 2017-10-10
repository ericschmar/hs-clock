import sys
from pprint import pprint

class deck:
    def __init__(self, id=None, game_length=None, turns=None, deck_id=None, deck_list=None, digest=None, win_rate=None, player_class=None):
        self.id = id
        self.game_length = game_length
        self.turns = turns
        self.deck_id = deck_id
        self.deck_list = deck_list
        self.digest = digest
        self.win_rate = win_rate
        self.player_class = player_class

    def print_deck(self):
        pprint(vars(self))
