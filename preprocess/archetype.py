import sys
from pprint import pprint

class archetype():
    def __init__(self, arch_id=None, name=None, player_class=None):
        self.arch_id = arch_id
        self.name = ''.join(e for e in name if e.isalnum())
        self.player_class = ''.join(e for e in player_class if e.isalnum())

    def print_archetype(self):
        pprint(vars(self))
