import sys
from pprint import pprint

class card:
    def __init__(self, id=None, name=None, cost=None, attack=None, health=None, card_type=None):
        self.id = id
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.type = card_type

    def print_card(self):
        pprint(self)