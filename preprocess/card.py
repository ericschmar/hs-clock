import sys
from pprint import pprint

class card:
    def __init__(self, id=None, name=None, cost=None, attack=None, health=None, card_type=None):
        self.id = id
        self.name = ''.join(e for e in name if e.isalnum())
        self.cost = cost
        self.attack = attack
        self.health = health
        self.card_type = ''.join(e for e in card_type if e.isalnum())

    def print_card(self):
        pprint(vars(self))